import games
import connection
import logging
import pprint

# TODO: move demos to their own testing file
def demo_sample():
    sample = games.load("game-data/sample.json")
    sample.info()

class Core():
    def __init__(self, game_path) -> None:
        self.logger = logging.getLogger(__name__) 
        self.logger.setLevel(logging.getLogger().getEffectiveLevel())

        self.game = games.load(game_path)
        if self.logger.level <= logging.INFO:
            self.game.info()

        self.conn = connection.connect()

    def loop(self):
        self.logger.info(self.game.addresses)
        
        game_state = {}
        for addr in self.game.addresses:
            game_state[addr] = 'None'

        self.logger.info(game_state)

        self.logger.info("Looping over memory values")
        while True:
            for addr in self.game.addresses:
                try:
                    logging.debug(f"Accessing {addr}")
                    read_val = self.conn.read_byte(addr)
                    game_state[addr] = int(read_val.decode('ascii')[1:])
                except Exception as e:
                    logging.debug(e)
                    logging.debug("SOCKET ACCESS ERROR")
                    continue

            pprint.pprint(game_state)

    