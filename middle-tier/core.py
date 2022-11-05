import games
import connection
import logging
import pprint

# TODO: move demos to their own testing file
def demo_sample():
    sample = games.load("game-data/sample.json")
    sample.info()

class Core():
    def __init__(self, game_path, config_info) -> None:
        # setup logging for class at the same level as root 
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.getLogger().getEffectiveLevel())

        # save config info
        self.config_info = config_info

        # load the currently supplied game data
        self.game = games.load(game_path)
        if self.logger.level <= logging.INFO:
            self.game.info()

        # connect to the BizHawk
        self.conn = connection.connect()

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

    