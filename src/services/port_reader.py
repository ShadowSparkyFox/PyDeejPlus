import serial.tools.list_ports
from src.domain.port import Port
from src.services import prompts


def serial_ports():
    ports = serial.tools.list_ports.comports()

    result = []

    for port, desc, hwid in sorted(ports):
        result.append(Port(port, desc))

    return result


def find_arduino():
    ports = serial_ports()

    i = 0
    hits = []
    the_arduino = -1
    for port in ports:
        if "Arduino" in port.port_desc:
            hits.append(i)
            the_arduino = i
        i += 1

    if len(hits) > 1:
        values_to_pass = []
        for hit in hits:
            values_to_pass.append(ports[hit])
        return prompts.prompt_user(values_to_pass, 'You have multiple Arduino\'s please pick one')
    elif len(hits) == 0 & the_arduino == -1:
        return prompts.prompt_user(ports, 'We did  not find an Arduino, please pick a COM port')
    else:
        return ports[the_arduino]
