import base64

from playwright.sync_api import sync_playwright
import os

if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="")
    args = parser.parse_args()

    if os.name == "nt":
        chromium_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    else:
        chromium_path = "/usr/bin/chromium-browser"

    output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
            }
        },
        "ver": 1
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, executable_path=chromium_path)
        page = browser.new_page()
        page.goto(args.url)
        screenshot_bytes = page.screenshot(full_page=True)
        output["plugin_result"]["biz"]["output"] = base64.b64encode(screenshot_bytes).decode()
        browser.close()

    print(json.dumps(output))
