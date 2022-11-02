import configparser
import logging
from tkinter.filedialog import askopenfilename


def check() -> None:
    config = configparser.ConfigParser()

    logger = logging.getLogger(__name__)    

    try:
        logger.info("Loading config")
        with open("config/middle-tier.ini") as config_file:
            config.read_file(config_file)
        logger.debug(f"bizhawk exe path: {config['directories']['bizhawk']}")

    except:
        logging.warning("No config found, setting up...")
        print("Where is the bizhawk excecutable?")
        dir_bizhawk = askopenfilename()

        config['directories'] = {
            "bizhawk": dir_bizhawk
        }

        with open('config/middle-tier.ini', 'w') as configfile:
            config.write(configfile)
    