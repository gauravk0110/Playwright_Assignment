from pages.playground_page import PlaygroundPage
from pages.simple_form_page import SimpleFormPage


def test_simple_form_shows_entered_message(page):
    greeting = "Welcome to TestMu AI"

    home = PlaygroundPage(page)
    home.open_playground()
    home.open_demo("Simple Form Demo")

    assert "simple-form-demo" in page.url
    page.wait_for_load_state("networkidle")

    form = SimpleFormPage(page)
    form.send_message(greeting)

    assert greeting in form.shown_message(greeting)