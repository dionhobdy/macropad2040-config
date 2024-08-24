# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name': 'missing keys',  # Application name
    'macros': [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6E6CF8, '`', ['`']),
        (0x6E6CF8, '~', ['~']),
        (0x6E6CF8, '', ['']),
        # 2nd row ----------
        (0xAC93FB, '', ['']),
        (0xAC93FB, '', ['']),
        (0xAC93FB, '', ''),
        # 3rd row ----------
        (0xF2F2FF, '', ['']),
        (0xF2F2FF, '', ['']),
        (0xF2F2FF, '', ['']),
        # 4th row ----------
        (0x407691, '', ['']),
        (0x407691, '', []),
        (0x407691, '', []),  # Hack-a-Day in new win
        # Encoder button ---
        (0xFFFFFF, '', [''])  # Open both FE and backend
    ]
}