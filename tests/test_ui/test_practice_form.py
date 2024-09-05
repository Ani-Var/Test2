from idlelib import browser

import allure
import pytest
from playwright.sync_api import Page
from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.practice_form.practice_start import PracticeStart
from base.pages.practice_form.practice_form_methods import PracticeFormMethods

class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Practice Form")
    @allure.title("Заполнение формы регистрации пользователя")
    def test_practice_form(self, page: Page, practice_form: PracticeFormPage):
        errors = []
        try:
            PracticeStart.practice_form(page, practice_form)

            errors.extend(PracticeFormMethods.fill_name_input(practice_form))
            errors.extend(PracticeFormMethods.fill_email(practice_form))
            errors.extend(PracticeFormMethods.select_gender(practice_form, 'Male'))
            errors.extend(PracticeFormMethods.fill_mobile_number(practice_form))

            errors.extend(PracticeFormMethods.fill_subjects(practice_form))
            errors.extend(PracticeFormMethods.check_hobbies(practice_form))

            errors.extend(PracticeFormMethods.submit_form(practice_form))
        except AssertionError as e:
            errors.append(str(e))
        page.screenshot(path='img/screenshot.png', full_page=True)  # Сохранение скриншота всей страницы
        print("Скриншот успешно сохранен как 'screenshot.png'")
        browser.close()

        if errors:
            pytest.fail(f"Тест завершился с ошибками: {', '.join(errors)}")