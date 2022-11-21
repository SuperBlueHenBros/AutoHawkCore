import json
import logging
import helper


class Game():
    def __init__(self, raw_info: dict) -> None:
        # TODO: make more logger more specific
        self.logger = logging.getLogger(__name__)  
        self.logger.setLevel(logging.getLogger().getEffectiveLevel())

        self.read(raw_info)
        self.addresses = self.get_addresses(self.mapping)
        self.status_map = self.create_status_map(self.mapping)

    def read(self, raw_info: dict) -> None:
        # create relevant variables from provided game file json
        try:
            self.name = raw_info['game']
            self.console = raw_info['console']
            self.mapping = raw_info['addresses']

        except IndexError as e:
            self.logger.error('Required field missing from game file')
            self.logger.exception(e)

    def get_addresses(self, mapping: dict) -> list:
        # create basic list of addresses from mapping dict
        addresses = []
        for element in mapping:
            converted_address = int(element['address'], base=16)
            addresses.append(converted_address)
        
        return addresses

    def info(self):
        # display game information
        helper.seperator(title="Game Info:")
        print("Name:", self.name)
        print("Console:", self.console)
        print("Addresses:", [hex(addr) for addr in self.addresses])
        helper.seperator()

    def create_status_map(self, map):
        status = {}
        for add_info in map:
            status[int(add_info['address'], 16)] = add_info['name']

        return status
        
    def display_game_status(self, game_state: dict):
        self.logger.info("displaying game status")
        game_status = ""
        for addr in game_state:
            game_status += f"{self.status_map[addr]}: {game_state[addr]}\n"
        self.logger.info(game_status)
            

def load(path: str) -> Game:
    # load a single game
    with open(path) as game_dir:
        game_raw = json.load(game_dir)
    
    game_info = Game(game_raw)
    
    return game_info
    

def loadall() -> list[Game]:
    # load all games in game dir
    pass