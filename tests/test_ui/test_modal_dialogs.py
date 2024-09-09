from idlelib import browser

import allure
import pytest
from playwright.sync_api import Page
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.modal_dialogs.modal_dialogs_start import ModalDialogsStart


class TestModalDialogs:

    @allure.epic("Тесты модальных диалогов")
    @allure.feature("Modal Dialogs")
    @allure.title("Проверка кнопок модального диалога")
    def test_modal_dialogs_form(self, page: Page, modal_dialogs_page: ModalDialogsPage):
        errors = []
        try:
            ModalDialogsStart.modal_dialogs(page, modal_dialogs_page)


        except AssertionError as e:
            errors.append(str(e))

        page.screenshot(path='img/screen_modal_dialogs.png', full_page=True)  # Сохранение скриншота всей страницы
        print("Скриншот успешно сохранен как 'screen_modal_dialogs.png'")
        browser.close()

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")
