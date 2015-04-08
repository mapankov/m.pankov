__author__ = 'pma'

from unittest import TestCase
from Lion import Lion
import unittest
import States

class LionTest(TestCase):
    # тест инициализации
    def test_init(self):
        lion = Lion(States.states[0], States.transitions)
        self.assertEqual(States.states[0], lion.CurrentState, 'CurrentState have wrong value')
        self.assertEqual(None, lion.CurrentSubject, 'CurrentSubject have wrong value')
        self.assertEqual(None, lion.CurrentAction, 'CurrentAction have wrong value')

    # тест на переход льва в новое состояние
    def test_changestate(self):
        lion = Lion(States.states[0], States.transitions)
        lionCurrentState = lion.CurrentState
        lionCurrentAction = lion.CurrentAction
        lionCurrentSubject = lion.CurrentSubject
        # лев должен перейти в другое состояние
        lion.setstate(States.subjects[0])
        self.assertNotEqual(lionCurrentState, lion.CurrentState, 'CurrentState not changed')
        self.assertNotEqual(lionCurrentAction, lion.CurrentAction, 'CurrentAction not changed')
        self.assertNotEqual(lionCurrentSubject, lion.CurrentSubject, 'CurrentSubject not changed')

    # тест на то, перешел ли лев в другое состояние
    def test_notchangestate(self):
        lion = Lion(States.states[0], States.transitions)
        lionCurrentState = lion.CurrentState
        lionCurrentAction = lion.CurrentAction
        lionCurrentSubject = lion.CurrentSubject
        # лев не должен перейти в другое состояние, т.к. передан неверный входной символ
        lion.setstate(0)
        self.assertEqual(lionCurrentState, lion.CurrentState, 'CurrentState changed')
        self.assertEqual(lionCurrentAction, lion.CurrentAction, 'CurrentAction changed')
        self.assertEqual(lionCurrentSubject, lion.CurrentSubject, 'CurrentSubject changed')

if __name__ == '__main__':
    unittest.main()
