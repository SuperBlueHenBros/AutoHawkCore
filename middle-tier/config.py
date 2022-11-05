import configparser
import os
import logging
import helper
import tkinter.filedialog 

def get() -> configparser.ConfigParser:
    pass

def check() -> None:
    config = configparser.ConfigParser()
    logger = logging.getLogger(__name__)   

    root = helper.get_root_path()
    if os.path.exists(root + '/game-data/'):
        dir_data = root + '/game-data/'
    else:
        print("Where is your game data located?")
        dir_data = tkinter.filedialog.askdirectory() # prompt user to select excecutable 

    # check if config file already exists
    logger.info("Loading config")
    dir_config = root + "/config/middle-tier.ini"
    logger.info(f"Checking dir {dir_config}")
    try:
        with open(dir_config) as config_file:
            config.read_file(config_file)
        logger.debug(f"bizhawk exe path: {config['directories']['bizhawk']}")
        logger.debug(f"data path: {config['directories']['data']}")

    # create config file if it doesn't
    except FileNotFoundError:
        logging.warning("No config found, setting up...")
        
        # bizhawk excecutable is currently unused
        # currently just saving for future use
        print("Where is the bizhawk excecutable?")
        dir_bizhawk = tkinter.filedialog.askopenfilename() # prompt user to select excecutable    

        config['directories'] = {
            "data": dir_data,
            "bizhawk": dir_bizhawk,
        }
        
        # create file
        with open('config/middle-tier.ini', 'w') as configfile:
            config.write(configfile)

        return 
    