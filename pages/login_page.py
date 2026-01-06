from playwright.sync_api import Page
import os
from dotenv import load_dotenv
load_dotenv()


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("WAVEBL_URL")
        self.email_input = page.get_by_placeholder("Enter you account email")
        self.password_input = page.get_by_placeholder("Enter you password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_text("Invalid Username or Password. Please try again.")
    def navigate(self):
        if not self.url:
            raise ValueError("WAVEBL_URL is missing in .env file")
        self.page.goto(self.url)
    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()