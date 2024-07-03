# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name': 'gitHub',  # Application name
    'macros': [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6E6CF8, 'init', ['git init\n']),
        (0x6E6CF8, 'AC', ['git add . & git commit -m ""', Keycode.LEFT_ARROW]),
        (0x6E6CF8, 'Remote', ['git remote add origin']),
        # 2nd row ----------
        (0xAC93FB, 'Pull', ['git pull\n']),
        (0xAC93FB, 'POM', ['git pull origin main\n']),
        (0xAC93FB, 'Push', 'git push\n'),
        # 3rd row ----------
        (0xF2F2FF, 'Main.B', ['git checkout main\n']),
        (0xF2F2FF, 'New.B', ['git checkout -b ']),
        (0xF2F2FF, 'Rnme.B', ['git branch -M ']),
        # 4th row ----------
        (0x407691, 'G.Hub', [Keycode.CONTROL, 'n', -Keycode.COMMAND, 'github.com\n']),
        (0x407691, '', []),
        (0x407691, '', []),  # Hack-a-Day in new win
        # Encoder button ---
        (0xFFFFFF, '', ['git status'])  # Open both FE and backend
    ]
}