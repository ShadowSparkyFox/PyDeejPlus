import keyboard


def read_keypress(key_id):
    if key_id == 1:
        keyboard.press_and_release('1')
    if key_id == 2:
        keyboard.press_and_release('2')
    if key_id == 3:
        keyboard.press_and_release('3')
    if key_id == 4:
        keyboard.press_and_release('4')
    if key_id == 5:
        keyboard.press_and_release('F13')
    elif key_id == 6:
        keyboard.press_and_release('F14')
    elif key_id == 7:
        keyboard.press_and_release('F15')
    elif key_id == 8:
        keyboard.press_and_release('F16')
    elif key_id == 9:
        keyboard.press_and_release('F17')
    elif key_id == 10:
        keyboard.press_and_release('F18')
    elif key_id == 11:
        keyboard.press_and_release('F19')
    elif key_id == 12:
        keyboard.press_and_release('F20')
    elif key_id == 13:
        keyboard.press_and_release('F21')
    elif key_id == 14:
        keyboard.press_and_release('F22')
    elif key_id == 15:
        keyboard.press_and_release('F23')
    elif key_id == 16:
        keyboard.press_and_release('F24')
