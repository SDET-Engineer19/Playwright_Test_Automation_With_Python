
from playwright.sync_api import Playwright, expect


def test_navigate_to_admin_menu(playwright: Playwright):
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
    page.get_by_role("listitem").filter(has_text="Admin")
    page.get_by_role("listitem").filter(has_text="Admin").click()
    expect(page.locator("//h6")).to_have_count(2)
    expect(page.locator("//h6").last).to_have_text("User Management")


def test_get_all_admin_dropdown_values(playwright: Playwright):
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
    page.get_by_role("listitem").filter(has_text="Admin")
    page.get_by_role("listitem").filter(has_text="Admin").click()
    page.get_by_role("navigation").filter(has_text="Topbar Menu").is_visible()
    top_menu_list = page.get_by_role("listitem").all()
    print(top_menu_list)
