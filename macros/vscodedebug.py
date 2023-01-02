from adafruit_hid.keycode import Keycode

app = {
    'name': 'vscode_debug',
    'macros': [
        # row 1
        (0x004915, 'tglbrk ', [Keycode.F9]),
        (0x004915, 'start ', [Keycode.F5]),
        (0x004915, 'stop ', [Keycode.SHIFT, Keycode.F5]),
        # row 2
        (0x004915, 'stpovr ', [Keycode.F10]),
        (0x004915, 'stpin ', [Keycode.F11]),
        (0x004915, 'stpout ', [Keycode.SHIFT, Keycode.F11]),
        # row 3
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # row 4
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # encoder
        (0x000000, '', [])
    ]
}

