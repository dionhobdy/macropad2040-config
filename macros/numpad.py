# Universal Numpad
from adafruit_hid.keycode import Keycode

app = {
    "name" : "numpad",
    "macros" : [
        # row 1
        (0x6E6CF8, "7", [Keycode.KEYPAD_SEVEN]),
        (0x6E6CF8, "8", [Keycode.KEYPAD_EIGHT]),
        (0x6E6CF8, "9", [Keycode.KEYPAD_NINE]),
        # row 2
        (0xAC93FB, "4", [Keycode.KEYPAD_FOUR]),
        (0xAC93FB, "5", [Keycode.KEYPAD_FIVE]),
        (0xAC93FB, "6", [Keycode.KEYPAD_SIX]),
        # row 3
        (0xF2F2FF, "1", [Keycode.KEYPAD_ONE]),
        (0xF2F2FF, "2", [Keycode.KEYPAD_TWO]),
        (0xF2F2FF, "3", [Keycode.KEYPAD_THREE]),
        # row 4
        (0x407691, ".", [Keycode.KEYPAD_PERIOD]),
        (0x407691, "0", [Keycode.KEYPAD_ZERO]),
        (0x407691, "ENTER", [Keycode.KEYPAD_ENTER]),
        # encoder
        (0xFFFFFF, '', [Keycode.ENTER])
    ]
}