# MACROPAD Hotkeys example: Custom Windows configuration.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Spotify',  # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Kill', [0.2, Keycode.ALT, Keycode.F4]),
        (0x000000, 'Minimize', [Keycode.WINDOWS, Keycode.PAGE_DOWN]),
        (0x000000, 'Mute', [[ConsumerControlCode.MUTE]]),
        # 2nd row ----------
        (0x000000, 'Prev', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x000000, 'Play/Pause', [ConsumerControlCode.PLAY_PAUSE]),
        (0x000000, 'Next', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 3rd row ----------
        (0x000000, 'Repeat', [Keycode.CONTROL, 'r']),
        (0x000000, 'Shuffle', [Keycode.CONTROL, 's']), 
        (0x000000, 'Like', [Keycode.ALT, Keycode.SHIFT, 'b']), #Like current song playing
        # 4th row ----------
        (0x000000, 'Queue', [Keycode.ALT, Keycode.SHIFT, 'q']),   # Queue
        (0x000000, 'Home', [Keycode.ALT, Keycode.SHIFT, 'h']),   # Home
        (0x000000, 'Liked', [Keycode.ALT, Keycode.SHIFT, 's']),  # Liked songs library
        # Encoder button ---
        (0xe50e00, 'SOUND', []) 
    ]
}