from idlelib import browser

import allure
import pytest
from playwright.sync_api import Page

from base.pages.date_picker.date_picker_methods import DatePickerMethods
from base.pages.date_picker.date_picker_page import DatePickerPage
from base.pages.date_picker.date_picker_start import DatePickerStart

class TestDatePicker:

    @allure.epic("Тесты потока 1")
    @allure.feature("Date Picker")
    @allure.title("Тестирование выбора даты")
    def test_date_picker(self, page: Page, date_picker: DatePickerPage):
        errors = []
        try:
            DatePickerStart.date_picker(page, date_picker)

            with allure.step("Получение выбранной даты"):
                selected_date = DatePickerMethods.get_selected_date(date_picker)
                assert selected_date == "2024-09-10", f"Выбранная дата не соответствует ожидаемой: {selected_date}"

            with allure.step("Выбор времени"):
                date_picker.date_picker.select_time("09:09 PM")

            with allure.step("Получение выбранной даты и времени"):
                selected_date_time = DatePickerMethods.get_selected_date_time(date_picker)
                assert selected_date_time == "2024-09-09 09:09 PM", f"Выбранная дата и время не соответствуют ожидаемым: {selected_date_time}"

            with allure.step("Закрытие календаря"):
                date_picker.date_picker.close_calendar()
        except AssertionError as e:
            errors.append(str(e))
        page.screenshot(path='img/screenDatePicker.png', full_page=True)
        print("Скриншот успешно сохранен как 'screenDatePicker.png'")
        browser.close()

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")
