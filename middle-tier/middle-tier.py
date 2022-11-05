import argparse
import logging
from tkinter.filedialog import askopenfilename
import config
import core



### Core Functions ###
def load_file() -> dict:
    filename = askopenfilename()



### Setup Functions ###
def setup_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
                    prog = 'middle-tier',
                    description = 'Middle-tier for interfacing between bizhawk and our AI',
                    epilog = 'This project still needs a new name :)')

    parser.add_argument('-d', '--demo', action='store_true',
                    help="Test demo using the sample config") 
    parser.add_argument('-g', '--game',
                    help="Select a specific game config file to use")
    parser.add_argument('-l', '--loop', action='store_true',
                    help="Continously display the state of all addresses in console")

    parser.add_argument('-v', '--verbose',
                    action='store_true')
    parser.add_argument('-vv', '--very_verbose', action='store_true')
    
    args = parser.parse_args()  

    if args.verbose:
        logger.setLevel(logging.INFO)
    elif args.very_verbose: 
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    return args



def setup_all():
    logger.info("Setting up")

    config_info = config.check()

    logger.info("Done setup")

    return config_info



### Logger Setup ###
logging.basicConfig()
logger = logging.getLogger() 



### Setup CLI Arguments ###
if __name__ == "__main__":
    args = setup_cli()



### Setup for CLI and Importing ###
conf = setup_all()



### Main Runtime ###
if __name__ == "__main__":
    if args.demo:
        logger.info("Running demo")
        core.demo_sample()
    elif args.game: 
        logger.info(f"Running game {args.game}")
        client = core.Core(args.game, conf)
        if args.loop:
            client.loop()
    if args.loop and not args.game:
        logger.error("No game selected!")
        