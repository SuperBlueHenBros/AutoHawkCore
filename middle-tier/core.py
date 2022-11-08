import games
import connection
import logging
import subprocess
import pprint
import time
import tkinter.filedialog 

class Core():
    def __init__(self, game_path, config_info, rom_path=None) -> None:
        # setup logging for class at the same level as root 
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.getLogger().getEffectiveLevel())

        # save config info
        self.config_info = config_info

        # load the currently supplied game data
        self.game = games.load(game_path)
        if self.logger.level <= logging.INFO:
            self.game.info()

        if not rom_path:
            rom_path = tkinter.filedialog.askopenfilename(title="Where is your game ROM located") 
        self.rom_path = rom_path

        # connect to the BizHawk
        self.conn = connection.connect()

    def spawn_emulator(self):
        '''
        Automatically open bizhawk with hook.lua running
        '''
        bizhawk_path = self.config_info["directories"]["bizhawk"]
        self.logger.debug(f"Running bizhawk located at: {bizhawk_path}")

        self.logger.debug(f"Using ROM located at: {self.rom_path}")

        hook_path = self.config_info["directories"]["hook"]
        self.logger.debug(f"Using hook.lua located at: {hook_path}")

        command_args = "--lua=" + hook_path
        self.logger.info(f"Running: {bizhawk_path} {command_args}")
        subprocess.Popen([bizhawk_path, self.rom_path, command_args])

        self.logger.info("waiting for emulator to initialize")
        time.sleep(6)
        
        # TODO: open ROM when that's added to the emulator

    def loop(self):
        '''
        Continually poll the emulator for memory information
        '''
        self.logger.info(self.game.addresses)
        
        # create a local map of all addresses to read
        game_state = {}
        for addr in self.game.addresses:
            game_state[addr] = 'None'

        self.logger.debug(f"Core:loop: initial game_state{game_state}")

        self.logger.info("Looping over memory values")
        # Read bytes from the socket until the script is killed
        while True:
            for addr in self.game.addresses:
                try:
                    read_val = self.conn.read_byte(addr)
                    game_state[addr] = int(read_val.decode('ascii')[1:])
                except Exception as e: # TODO: change to specific exception
                    # This error is weirdly common and I haven't figured out why
                    logging.debug(e)
                    logging.debug("SOCKET ACCESS ERROR")
                    continue

            pprint.pprint(game_state)

    