'''
Created on Jan 10, 2015

@author: fcmeng
'''

from blessings import Terminal
from key_handler import KeyHandler
import pexpect
import os, sys


class InteractiveMenuList(object):
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.func = []
        self.current = 0
        self.terminal = Terminal()
        self.key = KeyHandler()

    def register_action(self, text, func):
        self.menu.append(text)
        self.func.append(func)

    def render(self):
        os.system('clear')
        while 1:
            with self.terminal.location(0,0):
                print('[%d] {t.red} %-40s {t.normal}'.format(t=self.terminal) % (self.current, self.menu[self.current]))
                self.split()

            with self.terminal.location(0, 2):
                for i,choice in enumerate(self.menu):
                    symbol = ' >> %-2d '.format(t=self.terminal) %i if choice == self.menu[self.current] else '    %-2d '%i
                    print(symbol + choice)
                self.split()

            self.interact()

    def interact(self):
        pressed = self.key.read()
        if pressed == KeyHandler.CTRL_C:
            exit()
        if pressed == KeyHandler.UP or pressed == 'k':
            self.current = max(0, self.current - 1)
            return
        if pressed == KeyHandler.DOWN or pressed == 'j':
            self.current = min(len(self.menu) - 1, self.current + 1)
            return
        if pressed == KeyHandler.ENTER or pressed == KeyHandler.SPACE:
            with self.terminal.location(0, len(self.menu) + 4):
                self.func[self.current]()

    def split(self):
        template_string ='{t.green} ---- {t.yellow} ---- '*4+'{t.normal}'
        print(template_string.format(t=self.terminal))


    def associate(self, im):
        self.register_action(im.name, im.render)
        im.register_action('go back to %s'%self.name, self.render)

    def bind_exit(self):
        self.register_action('exit',exit)


if __name__ == '__main__':
    def p(s):
        print(s)

    im2 = InteractiveMenuList('menu 2')
    im = InteractiveMenuList('menu 1')
    im2.register_action('test1', lambda: p('-----1'))
    im2.register_action('test2', lambda: p('-----2'))
    # im2.register_action('back', im.render)
    im.register_action('hello1', lambda: p('world1'))
    im.register_action('hello2', lambda: p('world2'))
    # im.register_action('go', im2.render)
    im.associate(im2)
    im.bind_exit()
    im.render()

