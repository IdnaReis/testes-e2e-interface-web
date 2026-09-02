from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Métodos comuns a todas as páginas (Page Object Model)."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception:
            # Se algo (ex: um anúncio) estiver bloqueando o clique visual,
            # tenta clicar via JavaScript, que ignora esse bloqueio.
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)) is not None
        except Exception:
            return False

    def get_text(self, locator):
        return self.find(locator).text
