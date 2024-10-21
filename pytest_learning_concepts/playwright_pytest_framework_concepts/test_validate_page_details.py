from playwright.sync_api import expect


def test_verify_page_details(set_up):
    page = set_up
    expect(page).to_have_title("OrangeHRM")
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    page.wait_for_timeout(200)
    page.locator("//button[contains(@class,'orangehrm-login-button')]").click()
    page.wait_for_timeout(2000)
    page.locator("//h6[normalize-space()='Dashboard']").is_visible()


def test_verify_login_page_details(set_up):
    page = set_up
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    page.wait_for_timeout(200)
    page.locator("//button[contains(@class,'orangehrm-login-button')]").click()
    page.wait_for_timeout(200)
    page.locator("//div[@class='oxd-pie-chart']").first.is_visible()


def test_verify_login_button_isVisible(set_up):
    page = set_up
    page.locator("//input[@name='username']").is_visible()
    page.locator("//input[@name='password']").is_visible()
    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    page.wait_for_timeout(200)
    page.locator("//button[contains(@class,'orangehrm-login-button')]").click()
    page.wait_for_timeout(200)
    menu_list = page.locator("//div[@class='oxd-sidepanel-body']//li")
    expect(menu_list).to_have_count(12)
