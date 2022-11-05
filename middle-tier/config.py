import configparser
import logging
from tkinter.filedialog import askopenfilename


def check() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    logger = logging.getLogger(__name__)    

    # check if config file already exists
    try:
        logger.info("Loading config")
        with open("config/middle-tier.ini") as config_file:
            config.read_file(config_file)
        logger.debug(f"bizhawk exe path: {config['directories']['bizhawk']}")
    # create config file if it doesn't
    except:
        logging.warning("No config found, setting up...")
        print("Where is the bizhawk excecutable?")
        # bizhawk excecutable is currently unused
        # currently just saving for the sake of an example
        dir_bizhawk = askopenfilename() # prompt user to select excecutable

        config['directories'] = {
            "bizhawk": dir_bizhawk
        }

        # creat file
        with open('config/middle-tier.ini', 'w') as configfile:
            config.write(configfile)

    return config
    