'''
Created on Jan 10, 2015

@author: fcmeng
'''
class Action(object):
    def __init__(self, name, func):
        self.name = name
        self.func = func