import json

import keyboard
import serial

from src.domain.slider import Slider
from src.services import port_reader as reader
from src.services.volume_controller import control_volume, load_config


def main():
    load_config()
    port = open_port()

    main_loop(port)


def main_loop(port):
    while 1:
        line = port.readline()

        line = line.removesuffix(bytes("\r\n", "utf-8"))

        if bytes('SLIDERINFO-', "utf-8") in line:
            line = line.removeprefix(bytes('SLIDERINFO-', 'utf-8'))
            split = line.split(bytes("|", "utf-8"))

            i = 0
            for v in split:
                try:
                    control_volume(Slider("A{}".format(i), int(v)))
                except ValueError:
                    pass
                i += 1

        if bytes('KEYPRESS-', "utf-8") in line:
            key = int(line.removeprefix(bytes('KEYPRESS-', 'utf-8')))
            print(key)
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            break


def open_port():
    port = reader.find_arduino()
    port = serial.Serial(port=port.port_id)
    if not port.isOpen():
        port.open()
    return port


if __name__ == "__main__":
    main()
