__author__ = 'pma'

from unittest import TestCase
from Lion import Lion
import unittest
import States


class LionTest(TestCase):
    def test_init(self):
        lion = Lion(States.subjects[0], States.states[0], States.states[1], States.actions[0])
        self.assertEqual(States.subjects[0], lion.Subject, 'Subject have wrong value')
        self.assertEqual(States.states[0], lion.CurrentState, 'CurrentState have wrong value')
        self.assertEqual(States.states[1], lion.FollowingState, 'FollowingState have wrong value')
        self.assertEqual(States.actions[0], lion.FollowingAction, 'FollowingAction have wrong value')

if __name__ == '__main__':
    unittest.main()
