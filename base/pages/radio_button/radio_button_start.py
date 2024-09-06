import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.radio_button.radio_button_methods import RadioButtonMethods
from base.pages.radio_button.radio_button_page import RadioButtonPage

class RadioButtonStart:
    @staticmethod
    def radio_button_test(page: Page, radio_button_page: RadioButtonPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_radiobutton(page)

            with allure.step("Тестирование радио кнопок"):
                RadioButtonMethods.radio_button_yes(radio_button_page)
                RadioButtonMethods.radio_button_impressive(radio_button_page)
                RadioButtonMethods.radio_button_yes(radio_button_page)

        except AssertionError as e:
            errors.append(str(e))
        return errors
