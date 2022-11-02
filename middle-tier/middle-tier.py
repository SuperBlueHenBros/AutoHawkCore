import argparse
import logging
from tkinter.filedialog import askopenfilename
import config

def load_file() -> dict:
    filename = askopenfilename()

logging.basicConfig()
logger = logging.getLogger()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'middle-tier',
                    description = 'Middle-tier for interfacing between bizhawk and our AI',
                    epilog = 'This project still needs a new name :)')
    parser.add_argument('-g', '--game',
                    help="Select a game config file to use")
    parser.add_argument('-v', '--verbose',
                    action='store_true')
    parser.add_argument('-vv', '--very_verbose',
                    action='store_true')
    args = parser.parse_args()  

    if args.verbose:
        logger.setLevel(logging.INFO)
    elif args.very_verbose: 
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)
    
    logger.info("Setting up")

    config.check()

    logging.info("Done setup")
        



    


