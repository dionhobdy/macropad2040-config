from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name': 'sleep',
    'macros': [
        # row 1
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # row 2
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # row 3
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # row 4
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # encoder
        (0x000000, '', [Keycode.SHIFT, Keycode.CONTROL, ConsumerControlCode.EJECT]),
    ],
}
