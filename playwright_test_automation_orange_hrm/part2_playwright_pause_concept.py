from playwright.sync_api import Playwright, expect


def test_pause_the_script(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.locator("//button[contains(@class,'orangehrm-login-button')]").is_visible()
    page.get_by_placeholder("Username").is_visible()
    page.get_by_placeholder("Password").is_visible()
    page.pause()
    expect(page).to_have_title("OrangeHRM")
    print("After Launching URL, Pause the Script")
