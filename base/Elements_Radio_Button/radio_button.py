import allure
from playwright.sync_api import Page

class RadioButton:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        """
        Инициализация объекта RadioButton.

        :param page: Экземпляр страницы Playwright, на которой находится радиокнопка.
        :param locator: Локатор радиокнопки.
        :param name: Имя радиокнопки.
        """
        self.page = page
        self.locator = locator
        self.name = name

    def click(self) -> None:
        """
        Нажатие на радиокнопку.

        С этим методом выполняется клик по радиокнопке, используя её локатор.
        """
        with allure.step(f'Нажатие на радиокнопку с именем "{self.name}"'):
            self.page.locator(self.locator).click()

    def is_selected(self) -> bool:
        """
        Проверка, выбрана ли радиокнопка.

        :return: True, если радиокнопка выбрана, иначе False.
        """
        with allure.step(f'Проверка, выбрана ли радиокнопка с именем "{self.name}"'):
            is_checked = self.page.locator(self.locator).get_attribute("checked")
            return is_checked is not None

    def hover(self) -> None:
        """
        Наведение курсора на радиокнопку.

        С этим методом выполняется наведение курсора на радиокнопку.
        """
        with allure.step(f'Наведение курсора на радиокнопку с именем "{self.name}"'):
            self.page.locator(self.locator).hover()

    def check_class(self, class_name: str) -> None:
        """
        Проверка класса радиокнопки.

        :param class_name: Имя класса, который необходимо проверить.
        """
        with allure.step(f'Проверка класса радиокнопки с именем "{self.name}"'):
            classes = self.page.locator(self.locator).get_attribute("class")
            assert class_name in classes, f"{self.name} -> класс '{class_name}' не найден в {classes}"
