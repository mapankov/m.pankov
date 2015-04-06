__author__ = 'pma'

import States

# сначала лев голодный
LionCurrent = States.states[0]
# что лев увидел
LionSaw = None
# действие, которое совершит лев
LionDoes = None

while True:
    print('Состояние льва: ', LionCurrent)
    print()
    i = 0
    # выводим список того, что он может увидеть
    for subject in States.subjects:
        print(i, subject)
        i += 1
    print('* выход из программы')
    print()
    lock = True
    while lock:
        act = input('Выберите, что увидел лев: ')
        try:
            index = int(act)
            if 0 <= index <= len(States.subjects):
                lock = False
        except ValueError:
            if act == '*':
                quit()
    LionSaw = States.subjects[index]
    print()
    print('Состояние льва: ', LionCurrent)
    print('Лев увидел: ', LionSaw)
    for lion in States.transitions:
        if lion.Subject == LionSaw and lion.CurrentState == LionCurrent:
            LionDoes = lion.FollowingAction
            LionCurrent = lion.FollowingState
            print('Действие льва: ', lion.FollowingAction)
            break