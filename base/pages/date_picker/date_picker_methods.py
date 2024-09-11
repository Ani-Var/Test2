import allure
from base.pages.date_picker.date_picker_page import DatePickerPage

class DatePickerMethods:
    @staticmethod
    def select_date(date_picker: DatePickerPage, date: str):
        errors = []
        try:
            with allure.step(f"Выбор даты {date}"):
                date_picker.date_picker.select_date(date)
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def get_selected_date(date_picker: DatePickerPage, date: str):
        with allure.step("Получение выбранной даты"):
            return date_picker.date_picker.get_selected_date(date)

    @staticmethod
    def get_selected_date_time(date_picker: DatePickerPage, date: str, time: str):
        with allure.step("Получение выбранной даты и времени"):
            return f"{date_picker.date_picker.get_selected_date(date, time )} {date_picker.date_picker.get_selected_time()}"

