from adafruit_hid.keycode import Keycode

app = {
    'name': 'vscode',
    'macros': [
        # row 1
        (0x004915, 'cmdpal ', [Keycode.SHIFT, Keycode.COMMAND, 'p']),
        (0x004915, 'open ', [Keycode.COMMAND, 'o']),
        (0x004915, 'settings', [Keycode.COMMAND, ',']),
        # row 2
        (0x004915, 'selall', [Keycode.COMMAND, 'a']),
        (0x004915, 'copy ', [Keycode.COMMAND, 'c']),
        (0x004915, 'cut ', [Keycode.COMMAND, 'x']),
        # row 3
        (0x004915, 'paste ', [Keycode.COMMAND, 'v']),
        (0x004915, 'comment', [Keycode.COMMAND, '//']),
        (0x004915, 'format ', [Keycode.SHIFT, Keycode.ALT, 'f']),
        # row 4
        (0x004915, 'fndall ', [Keycode.SHIFT, Keycode.COMMAND, 'f']),
        (0x004915, 'find ', [Keycode.COMMAND, 'f']),
        (0x004915, 'openterm', [Keycode.SHIFT, Keycode.CONTROL, '`']),
        # encoder
        (0x004915, '', [Keycode.COMMAND, 'w'])
    ]
}
