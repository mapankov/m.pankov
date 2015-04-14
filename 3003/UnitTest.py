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
    # тест инициализации
    def test_init(self):
        lion = Lion(states[0], transitions)
        self.assertIn(lion.CurrentState,
                      lion.Transitions.keys(),
                      'Current state of lion is not contained in the table of transitions')
        self.assertEqual(states[0], lion.CurrentState, 'CurrentState have wrong value')
        self.assertEqual(None, lion.CurrentSubject, 'CurrentSubject have wrong value')
        self.assertEqual(None, lion.CurrentAction, 'CurrentAction have wrong value')

    # тест на переход льва в новое состояние
    def test_changestate(self):
        lion = Lion(states[0], transitions)
        self.assertIn(lion.CurrentState,
                      lion.Transitions.keys(),
                      'Current state of lion is not contained in the table of transitions')
        # запоминаем текущее состояние льва
        lionCurrentState = lion.CurrentState
        lionCurrentAction = lion.CurrentAction
        lionCurrentSubject = lion.CurrentSubject
        # лев должен перейти в другое состояние
        lion.setstate(subjects[0])
        self.assertIn(lion.CurrentSubject,
                      lion.Transitions.get(lion.CurrentState).keys(),
                      'Current subject is not contained in the table of transitions')

        temp = lion.Transitions.get(lionCurrentState).get(lion.CurrentSubject)

        self.assertEqual(temp.FollowingAction, lion.CurrentAction, 'CurrentAction changed incorrectly')
        self.assertEqual(temp.FollowingState, lion.CurrentState, 'CurrentState changed incorrectly')

        self.assertNotEqual(lionCurrentState, lion.CurrentState, 'CurrentState not changed')
        self.assertNotEqual(lionCurrentAction, lion.CurrentAction, 'CurrentAction not changed')
        self.assertNotEqual(lionCurrentSubject, lion.CurrentSubject, 'CurrentSubject not changed')

    # тест на то, перешел ли лев в другое состояние
    def test_notchangestate(self):
        lion = Lion(states[0], transitions)
        self.assertIn(lion.CurrentState,
                      lion.Transitions.keys(),
                      'Current state of lion is not contained in the table of transitions')
        lionCurrentState = lion.CurrentState
        lionCurrentAction = lion.CurrentAction
        lionCurrentSubject = lion.CurrentSubject
        # лев не должен перейти в другое состояние, т.к. передан входной символ,
        # не содержащийся в таблице переходов
        lion.setstate(subjects[1])
        self.assertIn(lion.CurrentSubject,
                      lion.Transitions.get(lion.CurrentState).keys(),
                      'Current subject is not contained in the table of transitions')

        temp = lion.Transitions.get(lionCurrentState).get(lion.CurrentSubject)

        self.assertEqual(temp.FollowingAction, lion.CurrentAction, 'CurrentAction changed incorrectly')
        self.assertEqual(temp.FollowingState, lion.CurrentState, 'CurrentState changed incorrectly')

        self.assertEqual(lionCurrentState, lion.CurrentState, 'CurrentState changed')
        self.assertEqual(lionCurrentAction, lion.CurrentAction, 'CurrentAction changed')
        self.assertEqual(lionCurrentSubject, lion.CurrentSubject, 'CurrentSubject changed')

if __name__ == '__main__':
    unittest.main()
