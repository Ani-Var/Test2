
from playwright.sync_api import Page
from base.Widgets_DatePicker.date_picker import DatePicker

class DatePickerPage:
    def __init__(self, page: Page):
        self.page = page

        """Локаторы для страницы: Выбор даты"""
        self.date_picker = DatePicker(page, locator='//*[@id="datePickerMonthYearInput"]', name='Дата')
        self.time = DatePicker(page, locator='//*[@id="dateAndTimePickerInput"]',name='Время')
        self.date_picker = DatePicker(page, locator='//*[@id="timePickerInput"]', name='Дата')

        """Ожидания"""
        self.Wait_date_picker ='//*[@id="datePickerMonthYearInput"]'
        self.Wait_time ='//*[@id="dateAndTimePickerInput"]'
        self.Wait_date_picker ='//*[@id="timePickerInput"]'
