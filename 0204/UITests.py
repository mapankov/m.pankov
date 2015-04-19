__author__ = 'pma'

import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class UITests(TestCase):
    # driver = webdriver.Remote(
    # command_executor = 'http://localhost:9515',
    # desired_capabilities={
    #        "browserName" : 'firefox'
    #    })

    def test_weather(self):
        driver = webdriver.Firefox()
        driver.get('http://www.yandex.ru')
        inputElement = driver.find_element_by_id('text')
        inputElement.send_keys('gjujlf')
        inputElement.submit()
        try:
            WebDriverWait(driver, 10).until(lambda drv: driver.title.lower().startswith('погода'))
            self.assertIn('погода', driver.title.lower(), 'Не удалось определить раскладку клавиатуры')
        finally:
            driver.quit()

    def test_load_virtual_keyboard(self):
        driver = webdriver.Firefox()
        driver.get('http://www.yandex.ru')
        driver.implicitly_wait(5)
        inputElement = driver.find_element_by_class_name('keyboard-loader')
        inputElement.click()
        driver.implicitly_wait(5)
        try:
            self.assertTrue(driver.find_element_by_class_name('b-keyboard-popup__bar').is_displayed(),
                'Не отображается виртуальная клавиатура')
        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()
