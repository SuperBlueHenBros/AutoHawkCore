import json
import logging
import pprint

class Game():
    def __init__(self, raw_info: dict) -> None:
        # TODO: make more logger more specific
        self.logger = logging.getLogger(__name__)  
        self.read(raw_info)

    def read(self, raw_info: dict):
        try:
            self.name = raw_info['game']
            self.console = raw_info['console']
            self.addresses = raw_info['addresses']

        except IndexError as e:
            self.logger.error('Required field missing from game file')
            self.logger.exception(e)

    def info(self):
        print(self.name)
        print(self.console)
        pprint.pprint(self.addresses)
        

def load(path: str) -> Game:
    # load a single game
    with open(path) as game_dir:
        game_raw = json.load(game_dir)
    
    game_info = Game(game_raw)
    
    return game_info
    

def loadall() -> list[Game]:
    # load all games in game dir
    pass