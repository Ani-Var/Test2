import allure
from base.pages.text_box.text_box_page import TextBoxPage

class TextBoxMethods:

    @staticmethod
    def fill_name_input(text_box_page: TextBoxPage):
        errors = []
        try:
            with allure.step("Ввод полного имени"):
                text_box_page.full_name.fill("Ани Вар")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def fill_email(text_box_page: TextBoxPage):
        errors = []
        try:
            with allure.step("Ввод электронной почты"):
                text_box_page.email.fill("aniVar@gmail.com")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def fill_current_address(text_box_page: TextBoxPage):
        errors = []
        try:
            with allure.step("Ввод текущего адреса"):
                text_box_page.current_address.fill("Улица Селезнева, дом 4")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def fill_permanent_address(text_box_page: TextBoxPage):
        errors = []
        try:
            with allure.step("Ввод постоянного адреса"):
                text_box_page.permanent_address.fill("Улица Ленина, дом 53")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def submit_form(text_box_page: TextBoxPage):
        errors = []
        try:
            with allure.step("Отправка формы"):
                text_box_page.submit_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors

