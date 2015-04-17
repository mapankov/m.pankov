from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PageObject import Page

__author__ = 'pma'


class Tests(TestCase):
    def setUp(self):
        # driver = webdriver.Remote(
        # command_executor = 'http://localhost:9515',
        # desired_capabilities={
        # "browserName" : 'firefox'
        # })
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open('http://www.yandex.ru')

    def tearDown(self):
        self.driver.close()

    def test_search_weather(self):
        self.page.open('http://www.yandex.ru')
        self.page.search_bar.search('gjujlf')
        try:
            WebDriverWait(self.driver, 10).until(lambda drv: self.page.title.lower().startswith('погода'))
            self.assertIn('погода', self.page.title.lower(), 'Не удалось определить раскладку клавиатуры')
        finally:
            return

    def test_open_virtual_keyboard(self):
        self.page.open('http://www.yandex.ru')
        self.page.search_bar.open_virtual_keyboard()
        try:
            self.assertTrue(self.page.search_bar.is_virtual_keyboard_displayed, 'Не отображается виртуальная клавиатура')
        finally:
            return

    def test_open_link(self):
        self.page.open('http://www.yandex.ru')
        old_url = self.page.current_url
        try:
            self.page.try_visit_link('Погода')
            self.assertNotEqual(old_url, self.page.current_url, 'Переход по ссылке не осуществлен')
        finally:
            return

if __name__ == '__main__':
    unittest.main()
