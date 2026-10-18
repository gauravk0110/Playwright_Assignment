import os
import pytest
from playwright.sync_api import sync_playwright

from config.settings import RUN_MODE
from config.browsers import CLOUD_COMBOS, LOCAL_COMBOS
from utils.lt_helper import build_grid_url, mark_test_status

COMBOS = CLOUD_COMBOS if RUN_MODE == "cloud" else LOCAL_COMBOS


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    setattr(item, "result_" + result.when, result)


@pytest.fixture(params=COMBOS, ids=[c["id"] for c in COMBOS])
def page(request):
    combo = request.param
    test_name = request.node.name

    with sync_playwright() as pw:
        if RUN_MODE == "cloud":
            # every browser on the grid is reached through the same endpoint
            browser = pw.chromium.connect(build_grid_url(combo, test_name), timeout=120000)
        else:
            show_browser = os.getenv("HEADED", "false").lower() == "true"
            browser = getattr(pw, combo["engine"]).launch(
                headless=not show_browser,
                slow_mo=400 if show_browser else 0,
            )

        context = browser.new_context(viewport={"width": 1366, "height": 768})
        tab = context.new_page()
        tab.set_default_timeout(15000)

        yield tab

        # work out the outcome of the test body
        body_result = getattr(request.node, "result_call", None)
        if RUN_MODE == "cloud":
            if body_result is not None and body_result.failed:
                mark_test_status(tab, "failed", "Test failed")
            else:
                mark_test_status(tab, "passed", "Test passed")
        elif body_result is not None and body_result.failed:
            tab.screenshot(path=f"reports/{test_name}_{combo['id']}.png")

        context.close()
        browser.close()