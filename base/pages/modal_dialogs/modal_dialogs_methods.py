import allure
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage

class ModalDialogsMethods:

    @staticmethod
    def open_small_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Открытие маленького модального диалога"):
                modal_dialogs.small_modal_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def close_small_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Закрытие маленького модального диалога"):
                modal_dialogs.small_modal_close_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def open_large_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Открытие большого модального диалога"):
                modal_dialogs.large_modal_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors

    @staticmethod
    def close_large_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Закрытие большого модального диалога"):
                modal_dialogs.large_modal_close_button.click()
        except AssertionError as e:
            errors.append(str(e))
        return errors
