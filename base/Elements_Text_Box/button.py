import allure
from base.Elements_Text_Box.component import Component

class Button(Component):
    @property
    def type_of(self) -> str:
        return 'кнопка'

    def click(self, **kwargs):
        with allure.step(f'Клик по {self.type_of} "{self.name}"'):
            self.should_be_visible()
            locator = self.get_locator(**kwargs)
            locator.click()