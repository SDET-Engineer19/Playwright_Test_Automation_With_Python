from playwright.sync_api import Page, Playwright, expect


def test_launch_browser(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_launch_chromium_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-demo.nopcommerce.com/login?")
    expect(page).to_have_title("Your store. Login")


def test_launch_firefox_browser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False, slow_mo=600)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-demo.nopcommerce.com/login?")
    expect(page).to_have_title("Your store. Login")


def test_launch_webkit_browser(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-demo.nopcommerce.com/login?")
    expect(page).to_have_title("Your store. Login")
