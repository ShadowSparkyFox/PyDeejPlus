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

    def __init__(self, config):
        self.config = config

    def control_volume(self, slider):
        value = get_percentage(slider)
        config = self.config[slider.id]
        if config is not None:
            set_volume(config, value)


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


def get_percentage(slider):
    percentage = 0.0
    if not slider.value == 0:
        percentage = Decimal(Decimal((slider.value / 1023)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    elif percentage < 0:
        percentage = 0.0

    return percentage
