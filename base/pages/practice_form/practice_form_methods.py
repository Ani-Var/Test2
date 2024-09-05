import allure
from base.pages.practice_form.practice_form_page import PracticeFormPage

class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill("Иван")
                practice_form.last_name.fill("Иванов")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def fill_email(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод электронной почты"):
                practice_form.email.fill("ivan.ivanov@Gmail.com")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def select_gender(practice_form: PracticeFormPage, gender: str):
        errors = []
        try:
            with allure.step(f"Выбор пола: {gender}"):
                if gender == 'Male':
                    practice_form.gender_male.click()
                elif gender == 'Female':
                    practice_form.gender_female.click()
                elif gender == 'Other':
                    practice_form.gender_other.click()
                else:
                    raise ValueError("Неверное значение пола")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def fill_mobile_number(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод мобильного номера"):
                practice_form.mobile_number.fill("8900241112")
        except AssertionError as e:
            errors.append(str(e))
        return errors



    @staticmethod
    def fill_subjects(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод предметов"):
                practice_form.subjects.fill("Математика")
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def check_hobbies(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Выбор хобби"):
                practice_form.hobbies.click()

        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def submit_form(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Отправка формы"):
                practice_form.submit_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors
