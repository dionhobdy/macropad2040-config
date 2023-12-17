from adafruit_hid.keycode import Keycode
import subprocess

app = {
    'name': 'batch repairs 2',
    'macros': [
        # row 1
        (0x999999, 'route', [subprocess.run([r""])]),
        (0x999999, 'tl-tk', [subprocess.run([r""])]),
        (0x999999, ' ', [subprocess.run([r""])]),
        # row 2
        (0x000000, ' ', [subprocess.run([r""])]),
        (0x000000, ' ', [subprocess.run([r""])]),
        (0x000000, ' ', [subprocess.run([r""])]),
        # row 3
        (0x000000, ' ', [subprocess.run([r""])]),
        (0x000000, ' ', [subprocess.run([r""])]),
        (0x000000, ' ', [subprocess.run([r""])]),
        # row 4
        (0x000000, ' ', [subprocess.run([r""])]),
        (0x000000, ' ', [subprocess.run([r""])]),
        (0x000000, ' ', [subprocess.run([r""])]),
        # encoder
        (0x000000, ' ', [Keycode.ENTER])
    ]
}