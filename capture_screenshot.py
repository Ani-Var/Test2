import allure
from playwright.sync_api import sync_playwright

from base.pages.authorization.authorization_method import AuthorizationMethod


def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Запускаем браузер в фоновом режиме
        page = browser.new_page()
        with allure.step("Открытие страницы"):
            AuthorizationMethod.auth_practice_form(page)
        # Замените URL на нужный вам
        page.screenshot(path='screenshot.png', full_page=True)  # Сохранение скриншота всей страницы
        print("Скриншот успешно сохранен как 'screenshot.png'")
        browser.close()

if __name__ == "__main__":
    take_screenshot()
