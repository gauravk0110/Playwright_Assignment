# TestMu AI Playground - Playwright (Python + pytest)

Automation for the three "Playwright 101" scenarios on the TestMu AI Selenium Playground.

## Layout
```
config/    settings + browser/OS combinations
pages/     page objects (one class per page)
tests/     the three scenarios
utils/     TestMu AI capability + status helper
conftest.py  browser fixture (cloud or local)
```

## Setup
```
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install             # only needed for local runs
cp .env.example .env           # add your LT_USERNAME and LT_ACCESS_KEY
```

## Run on TestMu AI (parallel: Win10 Chrome + macOS Catalina Firefox)
```
pytest -n 2
```
Network logs, video, console logs and screenshots are switched on in `utils/lt_helper.py`.

## Quick local run (no credentials needed)
```
RUN_MODE=local pytest -n 2
```

## Locators used
role, id, css attribute, placeholder, xpath, text.
