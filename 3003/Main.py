__author__ = 'pma'


from Lion import Lion
import States

# инициализируем льва
lion = Lion(States.states[0], States.transitions)

while True:
    # выводим текущее состояние льва
    print('Состояние льва: ', lion.CurrentState)
    print()
    i = 0
    out = ''
    # выводим список того, что он может увидеть
    for subject in States.subjects:
        out += '[{0} {1}]'.format(i, subject)
        i += 1
    out += '[* выход из программы]'
    print(out)
    print()
    lock = True
    while lock:
        subj = input('Выберите, что увидел лев: ')
        try:
            index = int(subj)
            if 0 <= index <= len(States.subjects):
                lock = False
        except ValueError:
            if subj == '*':
                lock = False
                quit()
        finally:
            if lock:
                # если произошла ошибка
                print('Выбран несуществующий входной символ!')
    print()
    # выводим предыдущее состояние льва
    print('Состояние льва: ', lion.CurrentState)
    # меняем его состояние
    lion.setstate(States.subjects[index])
    print('Лев увидел: ', lion.CurrentSubject)
    print('Действие льва: ', lion.CurrentAction)
