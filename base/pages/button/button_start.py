import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.button.button_methods import ButtonMethods
from base.pages.button.button_page import ButtonPage

class ButtonStart:
    @staticmethod
    def button_page(page: Page, button_page: ButtonPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_buttons_page(page)

            with allure.step("Клик на кнопки"):
                errors.extend(ButtonMethods.click_double_click_button(button_page))
                errors.extend(ButtonMethods.click_right_click_button(button_page))

        except AssertionError as e:
            errors.append(str(e))

        return errors