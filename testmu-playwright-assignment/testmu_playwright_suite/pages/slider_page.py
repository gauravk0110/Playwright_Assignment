from pages.base_page import BasePage


class SliderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def _slider_with_default(self, start_value):
        # locator type: css attribute selector
        return self.page.locator(f"input[type='range'][value='{start_value}']")

    def _value_label(self, slider):
        # locator type: xpath - the output sitting next to the slider
        return slider.locator("xpath=following::output[1]")

    def drag_slider(self, start_value, target):
        slider = self._slider_with_default(start_value)
        slider.scroll_into_view_if_needed()

        low = int(slider.get_attribute("min") or 0)
        high = int(slider.get_attribute("max") or 100)
        box = slider.bounding_box()

        # rough drag with the mouse to the expected position
        ratio = (target - low) / (high - low)
        y = box["y"] + box["height"] / 2
        start_x = box["x"] + box["width"] * ((start_value - low) / (high - low))
        end_x = box["x"] + box["width"] * ratio

        self.page.mouse.move(start_x, y)
        self.page.mouse.down()
        self.page.mouse.move(end_x, y, steps=15)
        self.page.mouse.up()

        # fine tune with keyboard in case the drag landed a bit off
        slider.focus()
        guard = 0
        while int(slider.input_value()) != target and guard < 30:
            key = "ArrowRight" if int(slider.input_value()) < target else "ArrowLeft"
            slider.press(key)
            guard += 1

        return self._value_label(slider)
