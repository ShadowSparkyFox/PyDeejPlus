from time import sleep

import keyboard
import win32api

VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
code_playpause = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
code_next = win32api.MapVirtualKey(VK_MEDIA_NEXT_TRACK, 0)
code_prev = win32api.MapVirtualKey(VK_MEDIA_PREV_TRACK, 0)


class KeyboardController:
    def __init__(self, config):
        self.config = config

    def read_input(self, stroke):
        if isinstance(self.config[stroke], str):
            if self.config[stroke] == "play-pause":
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, code_playpause)
            elif self.config[stroke] == "next":
                win32api.keybd_event(VK_MEDIA_NEXT_TRACK, code_next)
            elif self.config[stroke] == "previous":
                win32api.keybd_event(VK_MEDIA_PREV_TRACK, code_prev)
            else:
                keyboard.send(str(self.config[stroke]))
        else:
            for key in self.config[stroke]:
                keyboard.send(str(key))
                sleep(.1)
