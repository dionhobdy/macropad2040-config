from adafruit_hid.keycode import Keycode

app = {
    'name': 'vscode',
    'macros': [
        # row 1
        (0x6E6CF8, 'cmdpal ', [Keycode.SHIFT, Keycode.COMMAND, 'p']),
        (0x6E6CF8, 'open ', [Keycode.COMMAND, 'o']),
        (0x6E6CF8, 'settings', [Keycode.COMMAND, ',']),
        # row 2
        (0xAC93FB, 'selall', [Keycode.COMMAND, 'a']),
        (0xAC93FB, 'copy ', [Keycode.COMMAND, 'c']),
        (0xAC93FB, 'cut ', [Keycode.COMMAND, 'x']),
        # row 3
        (0xF2F2FF, 'paste ', [Keycode.COMMAND, 'v']),
        (0xF2F2FF, 'comment', [Keycode.COMMAND, '//']),
        (0xF2F2FF, 'format ', [Keycode.SHIFT, Keycode.ALT, 'f']),
        # row 4
        (0x407691, 'fndall ', [Keycode.SHIFT, Keycode.COMMAND, 'f']),
        (0x407691, 'find ', [Keycode.COMMAND, 'f']),
        (0x407691, 'openterm', [Keycode.SHIFT, Keycode.CONTROL, '`']),
        # encoder
        (0xFFFFFFf, '', [Keycode.COMMAND, 'w'])
    ]
}