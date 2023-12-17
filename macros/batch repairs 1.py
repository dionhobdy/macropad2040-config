from adafruit_hid.keycode import Keycode
import subprocess

app = {
    'name': 'batch repairs 1',
    'macros': [
        # row 1
        (0x999999, 'Dis Back', [subprocess.run([r""])]),
        (0x999999, 'Disk Tool', [subprocess.run([r""])]),
        (0x999999, 'DISM', [subprocess.run([r""])]),
        # row 2
        (0x999999, 'e/d camera', [subprocess.run([r""])]),
        (0x999999, 'e/d contacts', [subprocess.run([r""])]),
        (0x999999, 'e/d mic', [subprocess.run([r""])]),
        # row 3
        (0x999999, 'e/d fire', [subprocess.run([r""])]),
        (0x999999, 'h/r/s', [subprocess.run([r""])]),
        (0x999999, 'iponfig', [subprocess.run([r""])]),
        # row 4
        (0x999999, 'netsh', [subprocess.run([r""])]),
        (0x999999, 'netstat', [subprocess.run([r""])]),
        (0x999999, 'powercfg' [subprocess.run([r""])]),
        # encoder
        (0x999999, '', [Keycode.ENTER])
    ]
}