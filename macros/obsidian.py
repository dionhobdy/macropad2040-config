 
# MACROPAD Hotkeys example: Custom Windows configuration.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'obsidian',  # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6E6CF8, 'Close', [Keycode.CONTROL, 'w']),
        (0x6E6CF8, 'Minimize', [Keycode.WINDOWS, Keycode.PAGE_DOWN]),
        (0x6E6CF8, '+Note', [Keycode.CONTROL, 'n']),
        # 2nd row ----------
        (0xAC93FB, '<-Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0xAC93FB, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0xAC93FB, 'Tab->', [Keycode.CONTROL, Keycode.TAB]),
        # 3rd row ----------
        (0xF2F2FF, 'Underln', [Keycode.CONTROL, 'u']),
        (0xF2F2FF, 'Indent', [Keycode.CONTROL, 'i']),
        (0xF2F2FF, 'Bold', [Keycode.CONTROL, 'b']),
        # 4th row ----------
        (0x407691, 'Undo', [Keycode.CONTROL, 'z']),   # ctrl+s
        (0x407691, 'Copy', [Keycode.CONTROL,'c']),   # ctrl+c
        (0x407691, 'Paste', [Keycode.CONTROL, 'v']),  # ctrl+v
        # Encoder button ---
        (0xFFFFFF, 'SOUND', []) # Close window/tab
    ]
}