"""
Testes E2E — Fluxo de Login
Cobre: login com credenciais válidas e login com credenciais inválidas.

Usa a conta fixa definida em test_data.py — rode test_cadastro.py uma vez
antes, para garantir que essa conta exista no site.
"""
from pages.login_page import LoginPage
from test_data import TEST_EMAIL, TEST_PASSWORD


class TestLogin:

    def test_login_com_credenciais_validas(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)
        assert login_page.is_login_successful(), "Login válido deveria ter sucesso"

    def test_login_com_credenciais_invalidas(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login()
        login_page.login("usuario_inexistente@exemplo.com", "senhaErrada123")
        assert login_page.has_login_error(), "Deveria exibir mensagem de erro para credenciais inválidas"
