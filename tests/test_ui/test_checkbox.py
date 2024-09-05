from idlelib import browser

import allure
import pytest
from playwright.sync_api import Page
from base.pages.checkbox.checkbox_page import CheckboxPage
from base.pages.checkbox.checkbox_start import CheckboxStart
from base.pages.checkbox.checkbox_methods import CheckboxMethods

class TestCheckbox:
    @allure.epic("Тесты потока 1")
    @allure.feature("Checkbox Form")
    @allure.title("Проверка чекбоксов")
    def test_checkbox_form(self, page: Page, checkbox_page: CheckboxPage):
        errors = []
        try:
            CheckboxStart.checkbox_form(page, checkbox_page)

            errors.extend(CheckboxMethods.interact_with_checkboxes(checkbox_page))

        except AssertionError as e:
            errors.append(str(e))

        page.screenshot(path='img/screenCheckbox.png', full_page=True)  # Сохранение скриншота всей страницы
        print("Скриншот успешно сохранен как 'screenCheckbox.png'")
        browser.close()

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")

