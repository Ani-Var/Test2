import allure
from playwright.sync_api import Page

class DatePicker:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    def select_date(self, date: str):
        with allure.step(f"Выбор даты {date}"):
            self.page.locator(self.locator).fill(date)

    def get_selected_date(self):
        with allure.step("Получение выбранной даты"):
            return self.page.locator(self.locator).input_value()
