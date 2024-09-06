from playwright.sync_api import Page
from base.page_factory.input import Input
from base.page_factory.button import Button

class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы для страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Электронная почта')
        self.gender_male = Button(page, locator='//*[@for="gender-radio-1"]', name='Мужчина')
        self.gender_female = Button(page, locator='//*[@id="gender-radio-2"]', name='Женщина')
        self.gender_other = Button(page, locator='//*[@id="gender-radio-3"]', name='Другой')
        self.mobile_number = Input(page, locator='//*[@id="userNumber"]', name='Мобильный номер')

        self.subjects = Input(page, locator='//*[@id="subjectsInput"]', name='Предметы')
        self.hobbies = Button(page, locator='//*[@for="hobbies-checkbox-1"]', name='Спорт')  # Чекбокс Спорт

        self.submit_button = Button(page, locator='//*[@id="submit"]', name='Отправить')

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_gender_male ='//*[@for="gender-radio-1"]'
        self.Wait_mobile_number = '//*[@id="userNumber"]'
        self.Wait_subjects ='//*[@id="subjectsInput"]'
        self.Wait_hobbies ='//*[@for="hobbies-checkbox-1"]'
        self.Wait_submit_button = '//*[@id="submit"]'
