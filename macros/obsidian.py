 
# MACROPAD Hotkeys example: Custom Windows configuration.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Obsidian v1.1.9',  # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Close', [Keycode.CONTROL, 'w']),
        (0x000000, 'Minimize', [Keycode.WINDOWS, Keycode.PAGE_DOWN]),
        (0x000000, '+Note', [Keycode.CONTROL, 'n']),
        # 2nd row ----------
        (0x000000, '<-Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x000000, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x000000, 'Tab->', [Keycode.CONTROL, Keycode.TAB]),
        # 3rd row ----------
        (0x000000, 'Underln', [Keycode.CONTROL, 'u']),
        (0x000000, 'Indent', [Keycode.CONTROL, 'i']),
        (0x000000, 'Bold', [Keycode.CONTROL, 'b']),
        # 4th row ----------
        (0x000000, 'Undo', [Keycode.CONTROL, 'z']),   # ctrl+s
        (0x000000, 'Copy', [Keycode.CONTROL,'c']),   # ctrl+c
        (0x000000, 'Paste', [Keycode.CONTROL, 'v']),  # ctrl+v
        # Encoder button ---
        (0x000000, 'SOUND', []) # Close window/tab
    ]
}

