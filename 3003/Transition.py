__author__ = 'pma'

# вспомогательный класс для повышения читабельности кода
class Transition:
    def __init__(self, followingState, followingAction):
        self.FollowingState = followingState
        self.FollowingAction = followingAction
