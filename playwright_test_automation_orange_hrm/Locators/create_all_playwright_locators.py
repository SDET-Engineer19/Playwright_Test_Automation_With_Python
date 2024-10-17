from playwright.sync_api import Playwright, expect


def test_practice_playwright_locators_one(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/auth/login")

    # get by labels

    page.get_by_label("Username").is_visible()
    page.get_by_label("Password").is_visible()

    # get by placeholders

    page.get_by_placeholder("username").fill("Admin")
    page.get_by_placeholder("password").fill("admin123")
    # get by locators

    page.locator("//button[normalize-space()='Login']").is_visible()
    page.locator("//button[normalize-space()='Login']").click()

    page.wait_for_timeout(2000)

    # Assertions
    expect(page).to_have_title("OrangeHRM")

    context.close()
    browser.close()