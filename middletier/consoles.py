import helper

import logging
import json


class Console:
    def __init__(self, raw_info: dict, name: str) -> None:
        # TODO: make more logger more specific
        self.logger = logging.getLogger(__name__)  
        self.logger.setLevel(logging.getLogger().getEffectiveLevel())

        self.name = name
        self.read_info(raw_info)

    def read_info(self, raw_info):
        # Cores
        self.core = raw_info["cores"]["default"]
        self.cores = raw_info["cores"]["all"]

        # Domains
        self.domain = raw_info["domains"]["default"]
        self.domains = raw_info["domains"]["all"]

        # Buttons
        self.buttons = self.Buttons(raw_info["buttons"])

    def info(self):
        # display game information
        helper.seperator(title="Console Info:")
        print(f"Name: {self.name}")
        print(f"Cores: {self.cores}")
        print(f"Domains: {self.domains}")
        print(f"Buttons: {self.buttons.map}")
        helper.seperator()

    class Buttons:
        def __init__(self, all_buttons) -> None:
            self.logger = logging.getLogger(__name__)  
            self.logger.setLevel(logging.getLogger().getEffectiveLevel())
            self.map = all_buttons
            self.state = self.create(all_buttons)

        def create(self, all_buttons):
            self.logger.debug("Setting up button mapping")
            button_map = {}
            for button in all_buttons:
                button_map[button] = False
            
            self.logger.debug(f"Buttons configured: {button_map}")

            return button_map

        def press(self, pressed):
            if pressed in self.map:
                self.state[pressed] = not self.state[pressed]
            else:
                logging.error("THE BUTTON PRESSED DOES NOT EXIST")
            return self.state[pressed]


def load(path: str, console: str) -> Console:
    # load a single game
    with open(path) as console_dir:
        console_raw = json.load(console_dir)
    
    console_info = Console(console_raw[console], console)

    return console_info
    