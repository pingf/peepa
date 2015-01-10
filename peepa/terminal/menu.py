'''
Created on Jan 10, 2015

@author: fcmeng
'''

from .action import Action
        
class Menu(object):
    def __init__(self, name, level=0):
        self.name = name
        self.slots = []
        self.level = level
    
    def add_action(self, action): 
        self.slots.append(action)
    def add_menu(self, menu):    
        self.slots.append(menu)
    def pprint(self):
        for e in self.slots:
            if isinstance(e, Action): print('    '*self.level+e.name) 
            elif isinstance(e, Menu): 
                print(e.name)
                e.pprint() 
          
        


if __name__ == '__main__':
    menu0 = Menu('test2',1)
    menu0.add_action(Action('hello3','test'))
    menu0.add_action(Action('hello4','test'))
    menu = Menu('test1')
    menu.add_action(Action('hello1','test'))
    menu.add_action(Action('hello2','test'))
    menu.add_menu(menu0)
    menu.pprint()