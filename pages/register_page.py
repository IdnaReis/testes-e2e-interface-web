from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    ACCOUNT_INFO_TITLE = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS1 = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    ACCOUNT_CREATED = (By.XPATH, "//b[contains(text(),'Account Created!')]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def open_signup(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def start_signup(self, name, email):
        self.type_text(self.SIGNUP_NAME, name)
        self.type_text(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def fill_account_information(self, password, first_name, last_name, address,
                                  country, state, city, zipcode, mobile):
        self.type_text(self.PASSWORD, password)
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.ADDRESS1, address)
        self.driver.find_element(*self.COUNTRY).send_keys(country)
        self.type_text(self.STATE, state)
        self.type_text(self.CITY, city)
        self.type_text(self.ZIPCODE, zipcode)
        self.type_text(self.MOBILE_NUMBER, mobile)
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED)

    def continue_after_creation(self):
        self.click(self.CONTINUE_BUTTON)
