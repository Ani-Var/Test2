import allure
import pytest
from playwright.sync_api import Page
from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.radio_button.radio_button_start import RadioButtonStart

class TestRadioButton:

    @allure.epic("Тесты потока 1")
    @allure.feature("Radio Button")
    @allure.title("Тестирование радио кнопок")
    def test_radio_button(self, page: Page, radio_button_page: RadioButtonPage):

        errors = RadioButtonStart.radio_button_test(page, radio_button_page)

        page.screenshot(path='img/screenshot_radio_button.png', full_page=True)
        print("Скриншот успешно сохранен как 'screenshot_radio_button.png'")

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")
