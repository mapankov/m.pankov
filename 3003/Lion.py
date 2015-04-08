__author__ = 'pma'

from Transition import Transition

class Lion:
    # передаем начальное состояние льва и таблицу переходов
    def __init__(self, initState, transitionsTable):
        self.Transitions = transitionsTable
        self.CurrentState = initState
        self.CurrentAction = None
        self.CurrentSubject = None

    # в качестве параметра передаем один из входных символов
    def setstate(self, subject):
        try:
            # пытаемся получить новое состояние льва из таблицы переходов
            temp = self.Transitions.get(self.CurrentState).get(subject)
        except AttributeError:
            temp = None
        finally:
            # если все получилось удачно и таблица переходов содержит
            # объекты необходимого вида, осуществляем
            # перевод льва в новое состояние
            if temp is not None and type(temp) is Transition:
                self.CurrentSubject = subject
                self.CurrentState = temp.FollowingState
                self.CurrentAction = temp.FollowingAction
