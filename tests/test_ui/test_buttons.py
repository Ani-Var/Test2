from idlelib import browser

import allure
import pytest

from playwright.sync_api import Page
from base.pages.button.button_page import ButtonPage
from base.pages.button.button_start import ButtonStart

class TestButtons:

    @allure.epic("Тесты потока 1")
    @allure.feature("Buttons")
    @allure.title("Тестирование кнопок")
    def test_buttons(self, page: Page, button_page: ButtonPage):
        errors = []
        try:
            errors.extend(ButtonStart.button_page(page, button_page))
        except AssertionError as e:
            errors.append(str(e))
        page.screenshot(path='img\screenButtons.png', full_page=True)  # Сохранение скриншота всей страницы
        print("Скриншот успешно сохранен как 'screenButtons.png'")
        browser.close()

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")