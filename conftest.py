
import pytest

from base.pages.button.button_page import ButtonPage
from base.pages.date_picker.date_picker_page import DatePickerPage
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.radio_button.radio_button_page import RadioButtonPage
from src.config.playwright import PlaywrightConfig
from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.text_box.text_box_page import TextBoxPage
from playwright.sync_api import Page, sync_playwright, Browser
from base.pages.checkbox.checkbox_page import CheckboxPage

@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page(viewport=PlaywrightConfig.PAGE_VIEWPORT_SIZE)
        yield page
        browser.close()

def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if PlaywrightConfig.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=PlaywrightConfig.IS_HEADLESS,
        slow_mo=PlaywrightConfig.SLOW_MO
    )

@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)

@pytest.fixture(scope='function')
def text_box_page(page: Page) -> TextBoxPage:
    return TextBoxPage(page)

@pytest.fixture(scope='function')
def checkbox_page(page: Page) -> CheckboxPage:
    return CheckboxPage(page)

@pytest.fixture(scope='function')
def radio_button_page(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)

@pytest.fixture(scope='function')
def button_page(page: Page) -> ButtonPage:
    return ButtonPage(page)

@pytest.fixture(scope='function')
def modal_dialogs_page(page: Page) -> ModalDialogsPage:
    return ModalDialogsPage(page)

@pytest.fixture(scope='function')
def date_picker(page: Page) -> DatePickerPage:
    return DatePickerPage(page)