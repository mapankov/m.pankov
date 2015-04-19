__author__ = 'pma'


class BaseComponent(object):
    def __init__(self, driver, element=None):
        self.Driver = driver
        self.Element = element
