import allure
from base.page_factory.component import Component

class Checkbox(Component):
    @property
    def type_of(self) -> str:
        return 'чекбокс'

    def check(self, **kwargs) -> None:
        """
        Установка чекбокса.
        """
        with allure.step(f'Установка {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.check()

    def uncheck(self, **kwargs) -> None:
        """
        Снятие чекбокса.
        """
        with allure.step(f'Снятие {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.uncheck()

    def is_checked(self, **kwargs) -> bool:
        """
        Проверка, установлен ли чекбокс.
        """
        with allure.step(f'Проверка, установлен ли {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            return locator.is_checked()

    def is_visible(self, **kwargs) -> bool:
        """
        Проверка видимости чекбокса.
        """
        with allure.step(f'Проверка видимости {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            return locator.is_visible()
