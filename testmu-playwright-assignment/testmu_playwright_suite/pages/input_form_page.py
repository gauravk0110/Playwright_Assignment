from pages.base_page import BasePage


class InputFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # the footer has its own email field, so everything is searched inside the main form
        self.form = page.locator("form", has=page.locator("#inputEmail4"))
        self.submit_btn = self.form.get_by_role("button", name="Submit", exact=True)
        self.name_field = self.form.get_by_placeholder("Name", exact=True)
        self.country_dd = self.form.locator("select[name='country']")
        self.success_msg = page.get_by_text(
            "Thanks for contacting us, we will get back to you shortly."
        )

    def click_submit(self):
        self.submit_btn.click()

    def validation_text(self):
        """Message shown when the form is submitted empty."""
        custom = self.page.get_by_text("Please fill in the fields")
        if custom.count() > 0:
            return custom.first.inner_text()
        # otherwise the browser's own required-field tooltip
        return self.name_field.evaluate("el => el.validationMessage")

    def fill_form(self, data):
        f = self.form
        self.name_field.fill(data["name"])
        f.get_by_placeholder("Email", exact=True).fill(data["email"])
        f.get_by_placeholder("Password", exact=True).fill(data["password"])
        f.get_by_placeholder("Company", exact=True).fill(data["company"])
        f.get_by_placeholder("Website", exact=True).fill(data["website"])
        self.country_dd.select_option(label=data["country"])
        f.get_by_placeholder("City", exact=True).fill(data["city"])
        f.get_by_placeholder("Address 1", exact=True).fill(data["address1"])
        f.get_by_placeholder("Address 2", exact=True).fill(data["address2"])
        f.get_by_placeholder("State", exact=True).fill(data["state"])
        f.get_by_placeholder("Zip", exact=False).fill(data["zip"])