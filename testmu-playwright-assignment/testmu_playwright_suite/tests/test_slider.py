from pages.playground_page import PlaygroundPage
from pages.slider_page import SliderPage


def test_slider_moves_from_15_to_95(page):
    start_point = 15
    end_point = 95

    home = PlaygroundPage(page)
    home.open_playground()
    home.open_demo("Drag & Drop Sliders")

    sliders = SliderPage(page)
    label = sliders.drag_slider(start_point, end_point)

    assert label.inner_text().strip() == str(end_point)
