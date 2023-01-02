from adafruit_hid.keycode import Keycode

app = {
    'name': 'git',
    'macros': [
        # row 1
        (0x004915, 'add', ['git add .\n']),
        (0x004915, 'commit', ['git commit -m ']),
        (0x004915, 'push', ['git push origin ']),
        # row 2
        (0x004915, 'pull', ['git pull origin ']),
        (0x004915, 'main', ['main\n']),
        (0x004915, 'develop', ['develop\n']),
        # row 3
        (0x004915, 'merge', ['git merge ']),
        (0x004915, 'checkout', ['git checkout ']),
        (0x004915, '-b', ['-b ']),
        # row 4
        (0x004915, 'status', ['git status']),
        (0x004915, 'branch', ['git branch']),
        (0x004915, 'clone', ['git clone ']),
        # encoder
        (0x004915, '', [Keycode.ENTER])
    ]
}
