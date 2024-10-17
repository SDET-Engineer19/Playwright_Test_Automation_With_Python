from playwright.sync_api import Playwright, expect

"""
  1. page.get_by_role("attribute_name","Text")
  2. page.get
"""


def test_login_ecart_wix_app(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    expect(page).to_have_title("Home | playwright-practice")
    page.get_by_role("button", name="Log In").is_visible()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    print("Clicked on login button")
    page.get_by_role("button", name="Sign up with email").is_visible()
    page.get_by_role("button", name="Sign up with email").click()
    print("Clicked on Sign up with email button")
    page.locator("//input[contains(@id,'emailInput')]").is_visible()
    page.locator("//input[contains(@id,'emailInput')]").fill("symon.storozhenko@gmail.com")
    page.locator("//input[contains(@id,'passwordInput')]").is_visible()
    page.locator("//input[contains(@id,'passwordInput')]").fill("test1234")


def test_login_orange_hrm(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.locator("//button[contains(@class,'orangehrm-login-button')]").is_visible()
    page.locator("//button[contains(@class,'orangehrm-login-button')]").click()
    page.get_by_placeholder("Username").is_visible()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").is_visible()
    page.get_by_placeholder("Password").fill("admin123")
    page.locator("//button[contains(@class,'orangehrm-login-button')]").click()
    expect(page).to_have_title("OrangeHRM")
    context.close()
    browser.close()


