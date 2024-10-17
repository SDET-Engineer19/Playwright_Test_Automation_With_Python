import pytest
from playwright.sync_api import Playwright, expect, Page
from pytest_playwright.pytest_playwright import playwright


@pytest.fixture(scope='module')
def test_initialization(playwright: Playwright):
    print("************** TEST EXECUTION STARTED ******************")
    browser = playwright.chromium.launch(headless=False, slow_mo=2000,args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    yield
    print("************** TEST EXECUTION ENDED ******************")
    browser.close()
    page.close()


@pytest.mark.usefixtures("test_initialization")
def test_validate_username(page: Page):
    page.locator("//input[@name='username']").is_visible()


@pytest.mark.usefixtures("test_initialization")
def test_validate_password(page: Page):
    page.locator("//input[@name='password']").is_visible()
