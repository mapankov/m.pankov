__author__ = 'pma'

from Lion import Lion

# входные символы
subjects = ['антилопа', 'охотник', 'дерево']
# состояния льва
states = ['голодный', 'сытый']
# действия льва
actions = ['съесть', 'спать', 'убежать', 'смотреть']

# таблица переходов
transitions = []
transitions.append(Lion(subjects[0], states[0], states[1], actions[0]))
transitions.append(Lion(subjects[1], states[0], states[0], actions[2]))
transitions.append(Lion(subjects[2], states[0], states[0], actions[1]))
transitions.append(Lion(subjects[0], states[1], states[0], actions[1]))
transitions.append(Lion(subjects[1], states[1], states[0], actions[2]))
transitions.append(Lion(subjects[2], states[1], states[0], actions[3]))
