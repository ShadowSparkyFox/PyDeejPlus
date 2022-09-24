from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import POINTER, cast
from decimal import Decimal, ROUND_HALF_UP


class VolumeController:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    config = ["master", "spotify.exe", ["msedge.exe", "mailbird.exe"], "", "", "", ""]


def control_volume(slider):
    value = get_percentage(slider)
    print("slider {}".format(slider))
    set_volume(VolumeController.config[slider.id], value)


def get_percentage(slider):
    percentage = 0.0
    if not slider.value == 0:
        percentage = Decimal(Decimal((slider.value / 1023)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    elif percentage < 0:
        percentage = 0.0

    return percentage


def set_volume(config, value):
    if config == "master":
        print("setting value")
        VolumeController.volume.SetMasterVolumeLevelScalar(value, None)
    elif config == "mic":
        pass
    else:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name().lower() in config:
                volume = session.SimpleAudioVolume
                print("setting value")
                volume.SetMasterVolume(value, None)
