import allure
from playwright.sync_api import Page

class Dropdown:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        """
        Инициализация объекта Dropdown.

        :param page: Экземпляр страницы Playwright, на которой находится выпадающий список.
        :param locator: Локатор выпадающего списка.
        :param name: Имя выпадающего списка.
        """
        self.page = page
        self.locator = locator
        self.name = name

    def select(self, option_text: str) -> None:
        """
        Выбирает опцию в выпадающем списке по тексту.

        :param option_text: Текст опции, которую нужно выбрать.
        """
        with allure.step(f'Выбор опции "{option_text}" в выпадающем списке с именем "{self.name}"'):
            self.page.locator(self.locator).select_option(label=option_text)