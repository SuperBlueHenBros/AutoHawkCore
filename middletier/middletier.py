import middletier.config as config
import middletier.helper as helper
import middletier.core as core

import argparse
import logging


# Depending on your machine bizhawk may start too fast or slow
# This is fine but can cause errors as bizhawk might not be connectable
# If you want to decrease any socket errors on startup, increase this timer
STARTUP_DELAY = 6 # Seconds



### Setup Functions ###
def setup_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
                    prog = 'middle-tier',
                    description = 'Middle-tier for interfacing between bizhawk and our AI',
                    epilog = 'This project still needs a new name :)')


    parser.add_argument('-c', '--config', action='store_true',
                    help="Force running of first-time config setup") 
    parser.add_argument('-d', '--demo', action='store_true',
                    help="Test demo using the sample config") 
    parser.add_argument('-g', '--game',
                    help="Select a specific game config file to use")
    parser.add_argument('-l', '--loop', action='store_true',
                    help="Continously display the state of all addresses in console")
    parser.add_argument('-m', '--manual', action='store_true',
                    help="Don't automatically start bizhawk, let the user start it manually instead")
    parser.add_argument('-p', '--play', action='store_true',
                    help="(Warning: Buggy) Play the game yourself!")
    parser.add_argument('-r', '--rom',
                    help="Specify the path to the file you'll be opening")
                    

    parser.add_argument('-q', '--quiet', action='store_true',
                        help="Only log errors to stdout")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Log extra info to stdout")
    parser.add_argument('-vv', '--very_verbose', action='store_true',
                        help="Log all debug info to stdout")
    
    args = parser.parse_args()  

    if args.quiet:
        logger.setLevel(logging.ERROR)
    if args.verbose:
        logger.setLevel(logging.INFO)
    elif args.very_verbose: 
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    return args



### Pull Setup Info ###
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
    if args.config:
        logger.warning("Forcibly running config setup. This will delete any previously written configuration!")
        # prompt unless running silently
        if logger.level < logging.ERROR:
            confirmation = helper.get_user_confirmation(prompt="Are you sure you want to reset your configuraton? (Y/n)\n")
            if confirmation:
                config.create()
            else: 
                logger.info("Config file recreation denied")

    if args.game:
        logger.info(f"Running game {args.game}")

        client = core.Core(args.game, conf, rom_path=args.rom)

        if not args.manual:
            client.spawn_emulator(startup_delay=STARTUP_DELAY)
        if args.loop:
            client.loop(play=args.play)

    if args.loop and not args.game:
        logger.error("No game selected!")
        