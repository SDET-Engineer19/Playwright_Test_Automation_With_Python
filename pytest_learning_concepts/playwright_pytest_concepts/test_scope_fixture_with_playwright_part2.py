import pytest
from playwright.sync_api import Playwright, expect, Page


@pytest.fixture(scope="class")
def test_launch_chrome(playwright: Playwright):
    chrome_browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=['--start-maximized'])
    chrome_context = chrome_browser.new_context(no_viewport=True)
    page = chrome_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    yield
    chrome_context.close()
    chrome_browser.close()


@pytest.fixture(scope="class")
def test_launch_firefox(playwright: Playwright):
    firefox_browser = playwright.firefox.launch(headless=False, slow_mo=1000)
    firefox_context = firefox_browser.new_context(no_viewport=True)
    page = firefox_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    yield
    firefox_context.close()
    firefox_browser.close()


@pytest.mark.usefixtures("test_launch_chrome")
def test_validate_username_password_chrome(page: Page):
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()


@pytest.mark.usefixtures("test_launch_firefox")
def test_validate_username_password_firefox(page: Page):
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()
