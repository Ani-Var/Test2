from playwright.sync_api import Page
from base.Elements_Radio_Button.radio_button import RadioButton

class RadioButtonPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы для страницы: Радио кнопки"""
        self.yes_radio = RadioButton(page, locator='//*[@for="yesRadio"]', name='ДА')
        self.impressive_radio = RadioButton(page, locator='//*[@for="impressiveRadio"]', name='Впечатляет')
        self.no_radio = RadioButton(page, locator='//*[@for="noRadio"]', name='НЕТ')


        """Ожидания"""
        self.Wait_yes_radio = '//*[@for="yesRadio"]'
        self.Wait_impressive_radio = '//*[@for="impressiveRadio"]'
        self.Wait_no_radio = '//*[@for="noRadio"]'
