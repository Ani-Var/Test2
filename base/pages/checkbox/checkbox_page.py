import allure
from playwright.sync_api import Page
from base.Elements_Check_Box.checkbox import Checkbox
from base.Elements_Check_Box.button import Button

class CheckboxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы для чекбоксов"""
        self.checkbox_home = Checkbox(page, locator='//*[@for="tree-node-home"]', name='Дом')
        self.checkbox_documents = Checkbox(page, locator='//*[@for="tree-node-documents"]', name='Документы')
        self.checkbox_downloads = Checkbox(page, locator='//*[@for="tree-node-downloads"]', name='Загрузки')

        """Локатор для кнопки раскрытия списка"""
        self.expand_all_button = Button(page, locator='.rct-option-expand-all', name='Раскрыть все')

    def expand_all_checkboxes(self):
        with allure.step('Раскрытие всех чекбоксов'):
            self.page.wait_for_selector(self.expand_all_button.locator, state='visible')
            self.expand_all_button.click()

    def select_checkboxes(self):
        with allure.step('Выбор нескольких чекбоксов'):
            self.checkbox_home.check()
            self.checkbox_documents.check()
            self.checkbox_downloads.check()
