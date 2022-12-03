import middletier.games as games
import middletier.consoles as consoles

import logging
import subprocess
import pprint
import time
import tkinter.filedialog 
import pynput
import configparser
import bizhook

# note: this just exists for a demo, should be deleted after it's been shown working
key_translator = {
    pynput.keyboard.Key.left: "P1 Left",
    pynput.keyboard.Key.right: "P1 Right",
    pynput.keyboard.Key.up: "P1 Up",
    pynput.keyboard.Key.down: "P1 Down",
    pynput.keyboard.Key.enter: "P1 Start",
    pynput.keyboard.KeyCode.from_char('z'): "P1 A",
    pynput.keyboard.KeyCode.from_char('x'): "P1 B"
}

class Core():
    def __init__(self, game_path: str, config_info: configparser.ConfigParser, 
                rom_path=None) -> None:
        # setup logging for class at the same level as root 
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.getLogger().getEffectiveLevel())

        # save config info
        self.config_info = config_info

        # load the currently supplied game data
        self.game = games.load(game_path)
        if self.logger.level <= logging.INFO:
            self.game.info()

        # load the console data for the given game
        console_path = config_info["directories"]["consoles"]
        self.console = consoles.load(console_path, self.game.console)
        if self.logger.level <= logging.INFO:
            self.console.info()

        if not rom_path:
            rom_path = tkinter.filedialog.askopenfilename(title="Where is your game ROM located") 
        self.rom_path = rom_path

        # connect to the BizHawk
        self.conn = self.connect()

    def spawn_emulator(self, startup_delay: int = 6, load_state: bool = False):
        '''
        Automatically open bizhawk with hook.lua running
        '''
        bizhawk_path = self.config_info["directories"]["bizhawk"]
        self.logger.debug(f"Running bizhawk located at: {bizhawk_path}")

        rom_path = self.rom_path
        self.logger.debug(f"Using ROM located at: {rom_path}")

        hook_path = self.config_info["directories"]["hook"]
        self.logger.debug(f"Using hook.lua located at: {hook_path}")

        lua_arg = "--lua=" + hook_path
        if load_state:
            self.state_path = self.config_info["directories"]["data"] + "/" + self.game.state_path
            self.logger.debug(f"save_path: {self.state_path}")
            state_arg = "--load-state=" + self.state_path
            self.logger.info(f"Running: {bizhawk_path} {rom_path} {lua_arg} {state_arg}")
            biz_response = subprocess.Popen([bizhawk_path, rom_path, lua_arg, state_arg], shell=True, stdout=subprocess.PIPE)
        else:
            self.logger.info(f"Running: {bizhawk_path} {rom_path} {lua_arg}")
            biz_response = subprocess.Popen([bizhawk_path, rom_path, lua_arg], shell=True, stdout=subprocess.PIPE)

        self.logger.info("Waiting for emulator to initialize")
        time.sleep(startup_delay)
        self.logger.debug(f"args: {biz_response.args}")

    def send_input(self, button: str, state: bool = None):
        '''
        Send a given button to bizhawk.
        '''
        if button in self.console.buttons.map:
            if state:
                self.conn.send_input(key_name=button, key_state=state)
            else:
                state = self.console.buttons.press(button)
                self.conn.send_input(key_name=button, key_state=state)
        else:
            self.logger.error(f"Invalid button provided: {button}")
            self.logger.warning("Make sure you have the right console selected and the buttons are correct")


    def send_input_keyboard(self, keypress):
        '''
        Send a given pynput key to bizhawk.

        For testing usage only, use send_input when using as an API
        '''
        if keypress in key_translator:
            key_translated = key_translator[keypress]
            state = self.console.buttons.press(key_translated)
            self.logger.debug(f"pressed key: {keypress}/{key_translated} (state: {state})")
            self.conn.send_input(key_name=key_translated, key_state=state)
        else:
            self.logger.debug(f"{keypress} is not a valid button (type: {type(keypress)}")

    def connect(self):
        '''
        Create instance of connection to bizhawk API
        '''
        self.logger.info("Creating connection...")
        connection = bizhook.memory.Memory("RAM")
        self.logger.info("Connection created!")
        return connection


    def loop(self, play: bool = False):
        '''
        Continually poll the emulator for memory information
        '''
        self.logger.info(self.game.addresses)

        if play:
            # keyboard listener for testing
            listener = pynput.keyboard.Listener(on_press=self.send_input_keyboard)
            listener.start()  # start to listen on a separate thread
        
        # create a local map of all addresses to read
        game_state = {}
        for addr in self.game.addresses:
            game_state[addr] = 'None'

        self.logger.debug(f"Core:loop: initial game_state{game_state}")

        self.logger.info("Looping over memory values")
        printing_minimizer = 0
        print_reset = 10
        # Read bytes from the socket until the script is killed
        while True:
            self.conn.advance_frame(frames=6)
            for addr in self.game.addresses:
                try:
                    read_val = self.conn.read_byte(addr)
                    game_state[addr] = int(read_val.decode('ascii')[1:])
                except Exception as e: # TODO: change to specific exception
                    # This error is weirdly common and I haven't figured out why
                    logging.debug(e)
                    logging.debug("SOCKET ACCESS ERROR")
                    continue

            if printing_minimizer > print_reset:
                self.game.display_game_status(game_state)
                printing_minimizer = 0
            else: 
                printing_minimizer += 1
            
            # pprint.pprint(game_state)

