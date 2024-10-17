from playwright.sync_api import Playwright, expect


def test_take_full_page_screenshot(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.locator("//button[contains(@class,'orangehrm-login-button')]").is_visible()
    page.get_by_placeholder("Username").is_visible()
    page.get_by_placeholder("Password").is_visible()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.locator("//button[contains(@class,'orangehrm-login-button')]").click()
    expect(page).to_have_title("OrangeHRM")
    page.screenshot(path="homepage.png", full_page=True)
