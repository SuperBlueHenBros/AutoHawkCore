import configparser
import os
import logging
import helper
import tkinter.filedialog 

def check() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.getLogger().getEffectiveLevel()) 

    root = helper.get_root_path()

    dir_data = get_data_dir()
    if not os.path.exists(dir_data):
        print("Where is your game data located?")
        dir_data = tkinter.filedialog.askdirectory() # prompt user to select excecutable 

    # check if config file already exists
    logger.info("Loading config")
    dir_config_file = get_config_file()
    logger.info(f"Checking dir {dir_config_file}")
    if os.path.isfile(dir_config_file):
        with open(dir_config_file) as config_file:
            config.read_file(config_file)
        logger.debug(f"bizhawk exe path: {config['directories']['bizhawk']}")
        logger.debug(f"data path: {config['directories']['data']}")

    # create config file if it doesn't
    else:
        logging.warning("No config found, setting up...")
        
        # get bizhawk excecutable for when running manually
        print("Where is the bizhawk excecutable?")
        dir_bizhawk = tkinter.filedialog.askopenfilename(title="Where is your bizhawk excecutable?") 
        logger.debug(f"Given bizhawk path: {dir_bizhawk}")

        # get hook.lua path for automatically running with bizhawk
        dir_hook = get_hook_file()

        if not os.path.isfile(dir_hook):
            print("Where is your hook.lua (Did you run the setup script?)")
            dir_hook = tkinter.filedialog.askopenfilename(initialdir=root, title="Where is your hook.lua?")
            logger.debug(f"Given lua hook path: {dir_hook}")

        config['directories'] = {
            "data": dir_data,
            "hook": dir_hook,
            "bizhawk": dir_bizhawk,
        }
        
        # create the directory for the config file if it doesn't already exists
        dir_config = get_config_dir()
        os.makedirs(dir_config, exist_ok=True)
    
        # create config file
        with open(dir_config_file, 'w') as configfile:
            config.write(configfile)

    return config


### Path Functions ###
# consolidate every reoccuring path into a function
def get_config_dir() -> str:
    return helper.get_root_path() + '/config'

def get_config_file() -> str:
    return get_config_dir() + "/middle-tier.ini"

def get_data_dir() -> str:
    return helper.get_root_path() + '/game-data'

def get_lua_dir() -> str:
    return helper.get_root_path() + '/lib/lua-components'

def get_hook_file() -> str:
    return get_lua_dir() + '/hook.lua'