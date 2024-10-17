from playwright.sync_api import Playwright, expect, Locator


def test_get_menu_list(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
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
    expect(page.locator("//ul//li//a//span")).to_have_count(12)
    menu_list = page.locator("//ul//li//a//span").all_inner_texts()
    print(menu_list)
    print(type(menu_list))
    context.close()
    browser.close()
