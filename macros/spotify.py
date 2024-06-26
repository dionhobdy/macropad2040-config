# MACROPAD Hotkeys example: Custom Windows configuration.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Spotify',  # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6E6CF8, 'Kill', [0.2, Keycode.ALT, Keycode.F4]),
        (0x6E6CF8, 'Minimize', [Keycode.WINDOWS, Keycode.PAGE_DOWN]),
        (0x6E6CF8, 'Mute', [[ConsumerControlCode.MUTE]]),
        # 2nd row ----------
        (0xAC93FB, 'Prev', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0xAC93FB, 'Play/Pause', [ConsumerControlCode.PLAY_PAUSE]),
        (0xAC93FB, 'Next', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 3rd row ----------
        (0xF2F2FF, 'Repeat', [Keycode.CONTROL, 'r']),
        (0xF2F2FF, 'Shuffle', [Keycode.CONTROL, 's']), 
        (0xF2F2FF, 'Like', [Keycode.ALT, Keycode.SHIFT, 'b']), #Like current song playing
        # 4th row ----------
        (0x407691, 'Queue', [Keycode.ALT, Keycode.SHIFT, 'q']),   # Queue
        (0x407691, 'Home', [Keycode.ALT, Keycode.SHIFT, 'h']),   # Home
        (0x407691, 'Liked', [Keycode.ALT, Keycode.SHIFT, 's']),  # Liked songs library
        # Encoder button ---
        (0xFFFFFFf, 'SOUND', []) 
    ]
}