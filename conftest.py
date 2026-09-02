import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://automationexercise.com"
SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


@pytest.fixture(scope="function")
def driver():
    """Sobe uma instância do Chrome antes de cada teste e fecha ao final."""
    options = webdriver.ChromeOptions()
    # Descomente a linha abaixo para rodar sem abrir janela (modo headless)
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(10)
    drv.get(BASE_URL)

    yield drv

    drv.quit()


@pytest.fixture(autouse=True)
def screenshot_on_result(request, driver):
    """Tira print da tela ao final de cada teste (evidência), com nome baseado
    no nome do teste e se ele passou ou falhou."""
    yield
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    test_name = request.node.name
    outcome = "PASSOU" if not request.node.rep_call.failed else "FALHOU"
    path = os.path.join(SCREENSHOTS_DIR, f"{test_name}_{outcome}.png")
    try:
        driver.save_screenshot(path)
    except Exception:
        pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda o resultado do teste (passou/falhou) para uso na fixture de screenshot."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
