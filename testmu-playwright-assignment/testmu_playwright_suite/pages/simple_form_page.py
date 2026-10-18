from pages.base_page import BasePage
from playwright.sync_api import expect


class SimpleFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # the id "user-message" is reused on the page, so use the placeholder instead
        self.message_box = page.get_by_placeholder("Please enter your Message")
        self.show_button = page.get_by_role("button", name="Get Checked Value")

    def send_message(self, text):
        self.message_box.fill(text)
        self.show_button.click()

    def shown_message(self, expected_text):
        output = self.page.locator("#message")
        expect(output).to_contain_text(expected_text)
        return output.inner_text().strip()