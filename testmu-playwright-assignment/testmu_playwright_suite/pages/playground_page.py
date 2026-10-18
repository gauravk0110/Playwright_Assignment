from pages.base_page import BasePage


class PlaygroundPage(BasePage):
    """Landing page that lists all the demo links."""

    def open_playground(self):
        self.go_to()

    def open_demo(self, link_text):
        # locator type 1: role based
        self.page.get_by_role("link", name=link_text, exact=True).click()
