import games
import connection
import logging

# TODO: move demos to their own testing file
def demo_sample():
    sample = games.load("game-data/sample.json")
    sample.info()

def run(game_path: str):
    logger = logging.getLogger(__name__) 
    logger.setLevel(logging.getLogger().getEffectiveLevel())

    game = games.load(game_path)
    if logger.level <= logging.INFO:
        game.info()
    conn = connection.connect()

def loop():
    while True:
        pass
    