import serial

from domain.slider import Slider
from services import port_reader as reader
from services.config import Config
from services.keyboard_controller import KeyboardController
from services.volume_controller import VolumeController


def main():
    port = open_port()
    config = Config()
    volume_controller = VolumeController(config.sliders())
    keyboard_controller = KeyboardController(config.key_config())
    main_loop(port, volume_controller, keyboard_controller)

def main_loop(port, volume_controller, keyboard_controller):
    while port.isOpen():
        line = port.readline()

        line = line.removesuffix(bytes("\r\n", "utf-8"))
        if bytes('SLIDERINFO-', "utf-8") not in line: print(line)

        if bytes('SLIDERINFO-', "utf-8") in line:
            line = line.removeprefix(bytes('SLIDERINFO-', 'utf-8'))
            split = line.split(bytes("|", "utf-8"))

            i = 0
            for v in split:
                try:
                    volume_controller.control_volume(Slider("A{}".format(i), int(v)))
                except ValueError:
                    pass
                i += 1

        if bytes('KEYPRESS-', "utf-8") in line:
            stroke = int(line.removeprefix(bytes('KEYPRESS-', 'utf-8')))
            keyboard_controller.read_input(stroke)


def open_port():
    port = reader.find_arduino()
    port = serial.Serial(port=port.port_id)
    if not port.isOpen():
        port.open()
    return port


if __name__ == "__main__":
    main()
