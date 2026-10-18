from pages.playground_page import PlaygroundPage
from pages.input_form_page import InputFormPage

SUCCESS_TEXT = "Thanks for contacting us, we will get back to you shortly."

customer = {
    "name": "Sunil Saini",
    "email": "sunil.saini@example.com",
    "password": "Test@1234",
    "company": "Umbrella Corporation",
    "website": "https://www.umbrellacorp.com",
    "country": "United States",
    "city": "New York",
    "address1": "1680 School St",
    "address2": "Apt 946",
    "state": "New York",
    "zip": "10001",
}


def test_input_form_validation_and_submit(page):
    home = PlaygroundPage(page)
    home.open_playground()
    home.open_demo("Input Form Submit")

    form = InputFormPage(page)

    # submitting an empty form should complain about the required fields
    form.click_submit()
    error = form.validation_text()
    assert "fill" in error.lower(), f"unexpected validation text: {error!r}"

    # now fill everything properly and submit
    form.fill_form(customer)
    form.click_submit()

    assert form.success_msg.is_visible()
    assert SUCCESS_TEXT in form.success_msg.inner_text()
