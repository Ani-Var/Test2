import allure
from base.pages.checkbox.checkbox_page import CheckboxPage


class CheckboxMethods:

    @staticmethod
    def interact_with_checkboxes(checkbox_page: CheckboxPage):
        errors = []
        try:
            with allure.step("Раскрытие всех чекбоксов"):
                checkbox_page.expand_all_checkboxes()
                if not checkbox_page.expand_all_button.is_visible():
                    raise AssertionError("Кнопка 'Раскрыть все' не видна")

            with allure.step("Выбор чекбоксов"):
                checkbox_page.select_checkboxes()
                if not (checkbox_page.checkbox_home.is_checked() and
                        checkbox_page.checkbox_documents.is_checked() and
                        checkbox_page.checkbox_downloads.is_checked()):
                    raise AssertionError("Не все чекбоксы выбраны")

        except AssertionError as e:
            errors.append(str(e))

        return errors
