from adafruit_hid.keycode import Keycode

app = {
    'name': 'app_setup',
    'macros': [
        # row 1
        (0x6E6CF8, 'react', ['npx create-react-app ']),
        (0x6E6CF8, 'r-boot', ['npm i react-bootstrap --save \n']),
        (0x6E6CF8, 'native', ['npx create-expo-app@latest ']),
        # row 2
        (0xAC93FB, 'elect', ['npm install --save-dev electron \n']),
        (0xAC93FB, 'init', ['npm init \n']),
        (0xAC93FB, 'npm i', ['npm i --save ']),
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