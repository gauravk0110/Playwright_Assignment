CLOUD_COMBOS = [
    {"id": "win10-chrome", "browserName": "Chrome", "browserVersion": "latest", "platform": "Windows 10"},
    {"id": "mac-firefox", "browserName": "pw-firefox", "browserVersion": "latest", "platform": "MacOS Sonoma"},
]

# used only when RUN_MODE=local
LOCAL_COMBOS = [
    {"id": "local-chromium", "engine": "chromium"},
    {"id": "local-firefox", "engine": "firefox"},
]