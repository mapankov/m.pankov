__author__ = 'pma'

from Transition import Transition

# входные символы
subjects = ['антилопа', 'охотник', 'дерево']
# состояния льва
states = ['голодный', 'сытый']
# действия льва
actions = ['съесть', 'спать', 'убежать', 'смотреть']

# таблица переходов
transitions = {states[0]: {subjects[0]: Transition(states[1], actions[0]),
                           subjects[1]: Transition(states[0], actions[2]),
                           subjects[2]: Transition(states[0], actions[1])},
               states[1]: {subjects[0]: Transition(states[0], actions[1]),
                           subjects[1]: Transition(states[0], actions[2]),
                           subjects[2]: Transition(states[0], actions[3])}
               }

# print(transitions.get(states[1]).get(subjects[0]).FollowingAction)
