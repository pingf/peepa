from peepa import Action
from unittest import TestCase

class TestAction(TestCase):
    def test_init(self):
        action = Action('name','func')
            
        self.assertEqual(action.name, 'name')
        self.assertEqual(action.func, 'func')
        