from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_AS = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

    def open_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def login(self, email, password):
        self.type_text(self.LOGIN_EMAIL, email)
        self.type_text(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_visible(self.LOGGED_IN_AS)

    def has_login_error(self):
        return self.is_visible(self.LOGIN_ERROR)
