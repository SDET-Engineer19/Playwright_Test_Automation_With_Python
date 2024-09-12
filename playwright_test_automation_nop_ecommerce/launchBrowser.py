from playwright.sync_api import Page, Playwright, expect


def test_launchBrowser(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_launchChromiumBrowser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=600)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.set_default_timeout(2000)
    expect(page).to_have_title("OrangeHRM")