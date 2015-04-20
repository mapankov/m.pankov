__author__ = 'pma'

from unittest import TestCase
from Transition import Transition
from Lion import Lion
import unittest

# входные символы
subjects = ['антилопа', 'охотник']
# состояния льва
states = ['голодный', 'сытый']
# действия льва
actions = ['съесть', 'спать']
# таблица переходов
transitions = {states[0]: {subjects[0]: Transition(states[1], actions[0])},
               states[1]: {subjects[0]: Transition(states[0], actions[1])}
               }


class LionTest(TestCase):
    def setUp(self):
        self.lion = Lion(states[0], transitions)

    # тест инициализации
    def test_init(self):
        self.assertIn(self.lion.CurrentState,
                      self.lion.Transitions.keys(),
                      'Current state of lion is not contained in the table of transitions')
        self.assertEqual(states[0], self.lion.CurrentState, 'CurrentState have wrong value')
        self.assertEqual(None, self.lion.CurrentSubject, 'CurrentSubject have wrong value')
        self.assertEqual(None, self.lion.CurrentAction, 'CurrentAction have wrong value')

    # тест на переход льва в новое состояние
    def test_changestate(self):
        self.assertIn(self.lion.CurrentState,
                      self.lion.Transitions.keys(),
                      'Current state of lion is not contained in the table of transitions')
        # запоминаем текущее состояние льва
        lionCurrentState = self.lion.CurrentState
        lionCurrentAction = self.lion.CurrentAction
        lionCurrentSubject = self.lion.CurrentSubject
        # лев должен перейти в другое состояние
        self.lion.setstate(subjects[0])
        self.assertIn(self.lion.CurrentSubject,
                      self.lion.Transitions.get(self.lion.CurrentState).keys(),
                      'Current subject is not contained in the table of transitions')

        temp = self.lion.Transitions.get(lionCurrentState).get(self.lion.CurrentSubject)

        self.assertEqual(temp.FollowingAction, self.lion.CurrentAction, 'CurrentAction changed incorrectly')
        self.assertEqual(temp.FollowingState, self.lion.CurrentState, 'CurrentState changed incorrectly')

        self.assertNotEqual(lionCurrentState, self.lion.CurrentState, 'CurrentState not changed')
        self.assertNotEqual(lionCurrentAction, self.lion.CurrentAction, 'CurrentAction not changed')
        self.assertNotEqual(lionCurrentSubject, self.lion.CurrentSubject, 'CurrentSubject not changed')

    # тест на то, перешел ли лев в другое состояние
    def test_notchangestate(self):
        self.assertIn(self.lion.CurrentState,
                      self.lion.Transitions.keys(),
                      'Current state of lion is not contained in the table of transitions')
        lionCurrentState = self.lion.CurrentState
        lionCurrentAction = self.lion.CurrentAction
        lionCurrentSubject = self.lion.CurrentSubject
        # лев не должен перейти в другое состояние, т.к. передан входной символ,
        # не содержащийся в таблице переходов
        self.lion.setstate(subjects[1])
        self.assertNotIn(self.lion.CurrentSubject,
                      self.lion.Transitions.get(self.lion.CurrentState).keys(),
                      'Current subject is not contained in the table of transitions')

        temp = self.lion.Transitions.get(lionCurrentState).get(self.lion.CurrentSubject)

        self.assertNotEqual(temp.FollowingAction, self.lion.CurrentAction, 'CurrentAction changed incorrectly')
        self.assertNotEqual(temp.FollowingState, self.lion.CurrentState, 'CurrentState changed incorrectly')

        self.assertEqual(lionCurrentState, self.lion.CurrentState, 'CurrentState changed')
        self.assertEqual(lionCurrentAction, self.lion.CurrentAction, 'CurrentAction changed')
        self.assertEqual(lionCurrentSubject, self.lion.CurrentSubject, 'CurrentSubject changed')

if __name__ == '__main__':
    unittest.main()
