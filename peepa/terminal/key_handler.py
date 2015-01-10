import sys
import tty
import termios

class KeyHandler(object):
    # common
    LF = '\x0d'
    CR = '\x0a'
    ENTER = '\x0d'
    BACKSPACE = '\x7f'
    SUPR = ''
    SPACE = '\x20'

    # CTRL
    CTRL_A = '\x01'
    CTRL_B = '\x02'
    CTRL_C = '\x03'
    CTRL_D = '\x04'
    CTRL_E = '\x05'
    CTRL_F = '\x06'
    CTRL_Z = '\x1a'

    # ALT
    ALT_A = '\x1b\x61'

    # CTRL + ALT
    CTRL_ALT_A = '\x1b\x01'

    # cursors
    UP = '\x1b\x5b\x41'
    DOWN = '\x1b\x5b\x42'
    LEFT = '\x1b\x5b\x44'
    RIGHT = '\x1b\x5b\x43'

    CTRL_ALT_SUPER = '\x1b\x5b\x33\x5e'

    def __init__(self):
        pass
    def read_raw(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def read(self):
        c1 = self.read_raw()
        if ord(c1) != 0x1b:
            return c1
        c2 = self.read_raw()
        if ord(c2) != 0x5b:
            return (c1 + c2)
        c3 = self.read_raw()
        if ord(c3) != 0x33:
            return (c1 + c2 + c3)
        c4 = self.read_raw()
        return (c1 + c2 + c3 + c4)