
from playwright.sync_api import Page
from base.Elements_Button.button import Button

class ButtonPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы для кнопок"""
        self.double_click_button = Button(page, locator='//*[@id="doubleClickBtn"]', name='Дважды щелкните меня')
        self.right_click_button = Button(page, locator='//*[@id="rightClickBtn"]', name='Щелкните меня правой кнопкой мыши')



