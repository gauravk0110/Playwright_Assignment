from config.settings import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, path=""):
        self.page.goto(f"{BASE_URL}{path}", wait_until="domcontentloaded")

    def current_url(self):
        return self.page.url
