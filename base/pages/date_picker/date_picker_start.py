import allure
from playwright.sync_api import Page
from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.date_picker.date_picker_methods import DatePickerMethods
from base.pages.date_picker.date_picker_page import DatePickerPage

class DatePickerStart:
    @staticmethod
    def date_picker(page: Page, date_picker: DatePickerPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_date_picker(page)

            with allure.step("Выбор даты"):
                errors.extend(DatePickerMethods.select_date(date_picker, "2024-09-10"))
                errors.extend(DatePickerMethods.get_selected_date(date_picker, "2024-09-10"))
                errors.extend(DatePickerMethods.get_selected_date_time(date_picker,  "2024-09-09","09:09 PM"))

        except AssertionError as e:
            errors.append(str(e))
        return errors
