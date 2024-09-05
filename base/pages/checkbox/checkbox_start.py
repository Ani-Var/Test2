import allure
from playwright.sync_api import Page
from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.checkbox.checkbox_methods import CheckboxMethods
from base.pages.checkbox.checkbox_page import CheckboxPage

class CheckboxStart:
    @staticmethod
    def checkbox_form(page: Page, checkbox_page: CheckboxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.checkbox(page)

            with allure.step("Взаимодействие с чекбоксами"):
                errors.extend(CheckboxMethods.interact_with_checkboxes(checkbox_page))

        except AssertionError as e:
            errors.append(str(e))
        return errors
