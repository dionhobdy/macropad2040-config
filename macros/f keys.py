# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name': 'f keys',  # Application name
    'macros': [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6E6CF8, 'F1', [Keycode.F1]),
        (0x6E6CF8, 'F2', [Keycode.F2]),
        (0x6E6CF8, 'F3', [Keycode.F3]),
        # 2nd row ----------
        (0xAC93FB, 'F4', [Keycode.F4]),
        (0xAC93FB, 'F5', [Keycode.F5]),
        (0xAC93FB, 'F6', [Keycode.F6]),
        # 3rd row ----------
        (0xF2F2FF, 'F7', [Keycode.F7]),
        (0xF2F2FF, 'F8', [Keycode.F8]),
        (0xF2F2FF, 'F9', [Keycode.F9]),
        # 4th row ----------
        (0x407691, 'F10', [Keycode.F10]),
        (0x407691, 'F11', [Keycode.F11]),
        (0x407691, 'F12', [Keycode.F12]),  # Hack-a-Day in new win
        # Encoder button ---
        (0xFFFFFF, '', [''])  # Open both FE and backend
    ]
}