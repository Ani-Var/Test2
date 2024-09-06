from playwright.sync_api import Page

from base.base import BasePage
from src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def auth_practice_form(page: Page):
        BasePage.open_page(page, Url.AUTOMATION_PRACTICE_FORM)

    @staticmethod
    def text_box(page: Page):
        BasePage.open_page(page, Url.TEXT_BOX)

    @staticmethod
    def checkbox(page: Page):
        BasePage.open_page(page, Url.CHECKBOX)

    @staticmethod
    def auth_radiobutton(page: Page):
        BasePage.open_page(page, Url.RADIO_BUTTON)