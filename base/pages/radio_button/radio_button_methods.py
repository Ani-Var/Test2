import allure
from base.pages.radio_button.radio_button_page import RadioButtonPage

class RadioButtonMethods:


    @staticmethod
    def radio_button_yes(radio_button_page: RadioButtonPage):
        errors = []
        try:
            with allure.step("Выбор радио кнопки 'Yes'"):
                radio_button_page.yes_radio.click()
                assert radio_button_page.yes_radio.is_selected(), "Радио кнопка 'Yes' не выбрана"

        except AssertionError as e:
            errors.append(str(e))
        return errors


    @staticmethod
    def radio_button_impressive(radio_button_page: RadioButtonPage):
        errors = []
        try:
            with allure.step("Выбор радио кнопки 'Impressive'"):
                radio_button_page.impressive_radio.click()
                assert radio_button_page.impressive_radio.is_selected(), "Радио кнопка 'Impressive' не выбрана"

        except AssertionError as e:
            errors.append(str(e))
        return errors
