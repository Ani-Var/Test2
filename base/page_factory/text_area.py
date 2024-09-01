import allure
from playwright.sync_api import Page

class TextArea:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        """
        Инициализация объекта TextArea.

        :param page: Экземпляр страницы Playwright, на которой находится текстовая область.
        :param locator: Локатор текстовой области.
        :param name: Имя текстовой области.
        """
        self.page = page
        self.locator = locator
        self.name = name

    def fill(self, text: str) -> None:
        """
        Заполняет текстовую область указанным текстом.

        :param text: Текст, который нужно ввести в текстовую область.
        """
        with allure.step(f'Заполнение текстовой области с именем "{self.name}" текстом "{text}"'):
            self.page.locator(self.locator).fill(text)

    def clear(self) -> None:
        """
        Очищает текстовую область, заполняя её пустой строкой.
        """
        with allure.step(f'Очистка текстовой области с именем "{self.name}"'):
            self.page.locator(self.locator).fill('')

    def is_visible(self) -> bool:
        """
        Проверяет видимость текстовой области.

        :return: True, если текстовая область видима, иначе False.
        """
        with allure.step(f'Проверка видимости текстовой области с именем "{self.name}"'):
            return self.page.locator(self.locator).is_visible()

    def get_text(self) -> str:
        """
        Получает текущий текст из текстовой области.

        :return: Текущий текст из текстовой области.
        """
        with allure.step(f'Получение текста из текстовой области с именем "{self.name}"'):
            return self.page.locator(self.locator).input_value()