import json
from importlib.metadata import version
from urllib.parse import quote

from config.settings import (
    LT_USERNAME, LT_ACCESS_KEY, LT_GRID_URL, BUILD_NAME,
)


def build_grid_url(combo, test_name):
    """Create the websocket url (with capabilities) for one cloud session."""
    caps = {
        "browserName": combo["browserName"],
        "browserVersion": combo["browserVersion"],
        "LT:Options": {
            "platform": combo["platform"],
            "build": BUILD_NAME,
            "name": test_name,
            "user": LT_USERNAME,
            "accessKey": LT_ACCESS_KEY,
            "network": True,     # network logs
            "video": True,       # video recording
            "console": True,     # console logs
            "visual": True,      # screenshots / step by step
            # lets the grid pick a browser build that matches this client
            "playwrightClientVersion": version("playwright"),
        },
    }
    return LT_GRID_URL + quote(json.dumps(caps))


def mark_test_status(page, status, remark):
    """Tell the TestMu AI dashboard if the test passed or failed."""
    payload = {
        "action": "setTestStatus",
        "arguments": {"status": status, "remark": remark},
    }
    try:
        page.evaluate("_ => {}", "lambdatest_action: " + json.dumps(payload))
    except Exception as err:  # never let reporting break the test run
        print("could not set test status:", err)