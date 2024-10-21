from playwright.sync_api import Playwright, expect


def test_login_orange_hrm(playwright: Playwright) -> None:
    chrome_browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=['--start-maximized'])
    chrome_context = chrome_browser.new_context(no_viewport=True)
    page = chrome_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    page.wait_for_timeout(200)
    expect(page).to_have_title("OrangeHRM")


def test_validate_pie_charts(playwright: Playwright) -> None:
    chrome_browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=['--start-maximized'])
    chrome_context = chrome_browser.new_context(no_viewport=True)
    page = chrome_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    page.wait_for_timeout(200)
    expect(page).to_have_title("OrangeHRM")
    page.locator("//div[@class='oxd-pie-chart']").first.is_visible()