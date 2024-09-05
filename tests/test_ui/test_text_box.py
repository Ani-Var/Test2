from idlelib import browser

import allure
import pytest
from playwright.sync_api import Page
from base.pages.text_box.text_box_page import TextBoxPage
from base.pages.text_box.text_box_start import TextBoxStart
from base.pages.text_box.text_box_methods import TextBoxMethods

class TestTextBox:
    @allure.epic("Тесты потока 1")
    @allure.feature("Text Box")
    @allure.title("Заполнение формы текстового поля")
    def test_text_box_form(self, page: Page, text_box_page: TextBoxPage):
        errors = []
        try:
            TextBoxStart.text_box_form(page, text_box_page)

            errors.extend(TextBoxMethods.fill_name_input(text_box_page))
            errors.extend(TextBoxMethods.fill_email(text_box_page))
            errors.extend(TextBoxMethods.fill_current_address(text_box_page))
            errors.extend(TextBoxMethods.fill_permanent_address(text_box_page))
            errors.extend(TextBoxMethods.submit_form(text_box_page))
        except AssertionError as e:
            errors.append(str(e))

        page.screenshot(path='img/screenTextBox.png', full_page=True)  # Сохранение скриншота всей страницы
        print("Скриншот успешно сохранен как 'screenTextBox.png'")
        browser.close()

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")
