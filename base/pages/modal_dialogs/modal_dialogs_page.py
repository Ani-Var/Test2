from playwright.sync_api import Page
from base.page_factory.button import Button

class ModalDialogsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы для страницы: Модальные диалоги"""
        self.small_modal_button = Button(page, locator='//*[@id="showSmallModal"]', name='Кнопка маленького модального диалога')
        self.small_modal_close_button = Button(page, locator='//*[@id="closeSmallModal"]', name='Кнопка закрытия маленького модального диалога')
        self.large_modal_button = Button(page, locator='//*[@id="showLargeModal"]', name='Кнопка большого модального диалога')
        self.large_modal_close_button = Button(page, locator='//*[@id="closeLargeModal"]', name='Кнопка закрытия большого модального диалога')

        """Ожидания"""
        self.Wait_small_modal_button = '//*[@id="showSmallModal"]'
        self.Wait_small_modal_close_button = '//*[@id="closeSmallModal"]'
        self.Wait_large_modal_button = '//*[@id="showLargeModal"]'
        self.Wait_large_modal_close_button = '//*[@id="closeLargeModal"]'

