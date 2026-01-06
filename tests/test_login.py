import os

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_wavebl_page_load(page: Page):
    page.goto("https://sdu-sandbox-issuer.rnd.wavebl.com/")
    print(page.title())


def test_valid_login_elements_visibility(page: Page):
        login_page = LoginPage(page)
        login_page.navigate()

        expect(login_page.email_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()
        expect(login_page.login_button).to_be_enabled()
def test_invalid_login_error(page: Page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login("wrong@user.com", "123456")

        expect(page.get_by_text("Invalid Username or Password. Please try again.")).to_be_visible()

def test_valid_login(page: Page):
        login_page = LoginPage(page)
        login_page.navigate()
        user = os.getenv("WAVEBL_USER")
        password = os.getenv("WAVEBL_PASS")
        login_page.login(user, password)
        expect(page.get_by_role("heading", name="Hello, sysadmin")).to_be_visible(timeout=10000)