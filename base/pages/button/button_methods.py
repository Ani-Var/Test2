import allure
from base.pages.button.button_page import ButtonPage

class ButtonMethods:
    @staticmethod
    def click_double_click_button(buttons_page: ButtonPage):
        errors = []
        try:
            with allure.step("Нажатие на кнопку Double Click"):
                buttons_page.double_click_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def click_right_click_button(button: ButtonPage):
        errors = []
        try:
            with allure.step("Нажатие на кнопку Right Click"):
                button.right_click_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors


