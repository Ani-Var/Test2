from playwright.sync_api import Page
from base.page_factory.input import Input
from base.page_factory.button import Button

class TextBoxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы для страницы: Текстовое поле"""
        self.full_name = Input(page, locator='//*[@id="userName"]', name='Полное имя')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Электронная почта')
        self.current_address = Input(page, locator='//*[@id="currentAddress"]', name='Текущий адрес')
        self.permanent_address = Input(page, locator='//*[@id="permanentAddress"]', name='Постоянный адрес')
        self.submit_button = Button(page, locator='//*[@id="submit"]', name='Отправить')

        """Ожидания"""
        self.Wait_full_name = '//*[@id="userName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_current_address = '//*[@id="currentAddress"]'
        self.Wait_permanent_address = '//*[@id="permanentAddress"]'
        self.Wait_submit_button = '//*[@id="submit"]'
