__author__ = 'pma'

from selenium.webdriver.common.by import By
from BaseComponent import BaseComponent


class SearchBar(BaseComponent):
    selectors = {
                    'self': (By.ID, 'text'),
                    'input': (By.ID, 'text'),
                    'submit': (By.CLASS_NAME, 'suggest2-form__button'),
                    'virtual_keyboard_button': (By.CLASS_NAME, 'keyboard-loader'),
                    'virtual_keyboard': (By.CLASS_NAME, 'b-keyboard-popup__bar')
                }

    # выполняет поисковый запрос
    def search(self, query):
        self.Driver.find_element(self.selectors['input'][0], self.selectors['input'][1]).send_keys(query)
        self.Driver.find_element(self.selectors['submit'][0], self.selectors['submit'][1]).submit()

    # открывает виртуальную клавиатуру
    def open_virtual_keyboard(self):
        self.Driver.find_element(self.selectors['virtual_keyboard_button'][0],
                                 self.selectors['virtual_keyboard_button'][1]).click()

    @property
    def is_virtual_keyboard_displayed(self):
        return self.Driver.find_element(self.selectors['virtual_keyboard'][0],
                                        self.selectors['virtual_keyboard'][1]).is_displayed()
