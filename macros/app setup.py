from adafruit_hid.keycode import Keycode

app = {
    'name': 'app_setup',
    'macros': [
        # row 1
        (0x004915, 'react', ['npx create-react-app ']),
        (0x004915, 'r-boot', ['npm i react-bootstrap --save \n']),
        (0x004915, '', ['']),
        # row 2
        (0x004915, '', ['']),
        (0x004915, '', ['']),
        (0x004915, '', ['']),
        # row 3
        (0x004915, '', ['']),
        (0x004915, '', ['']),
        (0x004915, '', ['']),
        # row 4
        (0x004915, '', ['']),
        (0x004915, '', ['']),
        (0x004915, '', ['']),
        # encoder
        (0x004915, '', [Keycode.ENTER])
    ]
}
