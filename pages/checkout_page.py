from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    PRODUCTS_LINK = (By.XPATH, "//a[contains(text(),'Products')]")
    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, ".product-image-wrapper")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".product-overlay .add-to-cart")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    CART_LINK = (By.XPATH, "//a[contains(text(),'Cart')]")
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")

    COMMENT_BOX = (By.CSS_SELECTOR, "textarea[name='message']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[contains(text(),'Place Order')]")

    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.ID, "submit")

    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]")

    def add_first_product_to_cart(self):
        self.click(self.PRODUCTS_LINK)

        # O botão "Add to Cart" só fica visível ao passar o mouse (hover)
        # sobre o card do produto, então simulamos o hover antes de clicar.
        product_card = self.find(self.FIRST_PRODUCT_CARD)
        ActionChains(self.driver).move_to_element(product_card).perform()

        add_to_cart_btn = self.find(self.ADD_TO_CART_BUTTONS)
        self.driver.execute_script("arguments[0].click();", add_to_cart_btn)

        # Fecha o modal "Added!" clicando em "Continue Shopping", se aparecer
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
            ).click()
        except Exception:
            pass

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)

    def place_order(self, comment=""):
        if comment:
            self.type_text(self.COMMENT_BOX, comment)
        self.click(self.PLACE_ORDER_BUTTON)

    def fill_payment_details(self, name_on_card, card_number, cvc, month, year):
        self.type_text(self.NAME_ON_CARD, name_on_card)
        self.type_text(self.CARD_NUMBER, card_number)
        self.type_text(self.CVC, cvc)
        self.type_text(self.EXPIRY_MONTH, month)
        self.type_text(self.EXPIRY_YEAR, year)
        self.click(self.PAY_BUTTON)

    def is_order_successful(self):
        return self.is_visible(self.ORDER_SUCCESS_MESSAGE)
