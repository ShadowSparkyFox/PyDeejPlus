from os.path import exists

import yaml
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import POINTER, cast
from decimal import Decimal, ROUND_HALF_UP


class VolumeController:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    config = {}
    path = "config.yaml"


def control_volume(slider):
    value = get_percentage(slider)
    config = VolumeController.config[slider.id]
    if config is not None:
        set_volume(config, value)


def get_percentage(slider):
    percentage = 0.0
    if not slider.value == 0:
        percentage = Decimal(Decimal((slider.value / 1023)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    elif percentage < 0:
        percentage = 0.0

    return percentage


def set_volume(config, value):
    if config == "master":
        VolumeController.volume.SetMasterVolumeLevelScalar(value, None)
    elif config == "mic":
        pass
    else:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name().lower() in config:
                volume = session.SimpleAudioVolume
                volume.SetMasterVolume(value, None)


def load_config():
    if not exists(VolumeController.path):
        file = open(VolumeController.path, "x")
        file.write("# Thank you for using PyDeejPlus\n"
                   "# For every slider you can add an entry, every entry can control:\n"
                   "# master volume with master, microphone with mic or an executable by {name}.exe\n"
                   "# below I have supplied you with an example setup\n"
                   "A0: master\n"
                   "A1: spotify.exe\n"
                   "A2: \n"
                   "    - msedge.exe\n"
                   "    - vlc.exe\n"
                   "A3: \n"
                   "A4: \n"
                   "A5: \n"
                   "A6: \n"
                   "A7: \n")
        file.close()
    VolumeController.config = yaml.load(open(VolumeController.path), Loader=yaml.FullLoader)
