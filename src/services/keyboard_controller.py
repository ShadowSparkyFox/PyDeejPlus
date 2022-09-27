from collections.abc import Sequence
from time import sleep

import keyboard

class KeyboardController:
    def __init__(self, config):
        self.config = config

    def read_input(self, stroke):
        if isinstance(self.config[stroke], str):
            keyboard.send(str(self.config[stroke]))
        else:
            for key in self.config[stroke]:
                keyboard.send(str(key))
                sleep(.1)
