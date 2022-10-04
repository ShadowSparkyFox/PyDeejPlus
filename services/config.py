from os.path import exists

import yaml


class Config:
    def __init__(self):
        self.config = load_config()

    def sliders(self):
        return self.config["sliders"]

    def key_config(self):
        return self.config["keys"]


def load_config():
    path = "config.yaml"
    if not exists(path):
        file = open(path, "x")
        file.write("# Thank you for using PyDeejPlus\n"
                   "# For every slider you can add an entry, every entry can control:\n"
                   "# master volume with master, microphone with mic or an executable by {name}.exe\n"
                   "# below I have supplied you with an example setup\n"
                   "sliders:\n"
                   "    A0: master\n"
                   "    A1: spotify.exe\n"
                   "    A2: \n"
                   "        - msedge.exe\n"
                   "        - vlc.exe\n"
                   "    A3: \n"
                   "    A4: \n"
                   "    A5: \n"
                   "    A6: \n"
                   "    A7: \n"
                   "# Below you can enter shortcuts of your choice\n"
                   "# Letter, number, F keys, or combine with a modifier => Shift+A, Ctrl+c, ...\n"
                   "keys: \n"
                   "    1: \"a\"\n"
                   "    2: \"b\"\n"
                   "    3: \"c\"\n"
                   "    4: \"d\"\n"
                   "    5: \"e\"\n"
                   "    6: \"f\"\n"
                   "    7: \"g\"\n"
                   "    8: \"h\"\n"
                   "    9: \"i\"\n"
                   "    10: \"j\"\n"
                   "    11: \"k\"\n"
                   "    12: \"l\"\n"
                   "    13: \"m\"\n"
                   "    14: \"n\"\n"
                   "    15: \"o\"\n"
                   "    16: \"p\"\n"
                   "")
        file.close()
    return yaml.load(open(path), Loader=yaml.FullLoader)
