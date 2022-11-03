import games

# TODO: move demos to their own testing file
def demo_sample():
    sample = games.load("game-data/sample.json")
    sample.info()

def run(game_path: str):
    logger = logging.getLogger(__name__) 
    logger.setLevel(logging.getLogger().getEffectiveLevel())

    game = games.load(game_path)
    game.info()