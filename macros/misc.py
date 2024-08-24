from adafruit_hid.keycode import Keycode

app = {
    'name': 'sleep mode',
    'macros': [
        # row 1
        (0x6E6CF8, '', ['']),
        (0x6E6CF8, '', ['']),
        (0x6E6CF8, '', ['']),
        # row 2
        (0xAC93FB, '', ['']),
        (0xAC93FB, '', ['']),
        (0xAC93FB, '', ['']),
        # row 3
        (0xF2F2FF, '', ['']),
        (0xF2F2FF, '', ['']),
        (0xF2F2FF, '', ['']),
        # row 4
        (0x407691, '', ['']),
        (0x407691, '', ['']),
        (0x407691, '', ['']),
        # encoder
        (0xFFFFFF, '', [Keycode.ENTER])
    ]
}