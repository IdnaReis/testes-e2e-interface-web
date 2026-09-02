"""
Testes E2E — Fluxo de Cadastro (Signup)
Cobre: criação de uma nova conta de usuário do início ao fim.

Rode este arquivo UMA VEZ para criar a conta fixa definida em test_data.py.
Se rodar de novo, o site vai acusar "Email Address already exist!" — nesse
caso o teste é pulado automaticamente (não é uma falha, só um aviso).
"""
import pytest
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage
from test_data import TEST_EMAIL, TEST_PASSWORD, TEST_NAME

EMAIL_EXISTS_LOCATOR = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")


class TestCadastro:

    def test_criar_nova_conta_com_sucesso(self, driver):
        register_page = RegisterPage(driver)

        register_page.open_signup()
        register_page.start_signup(TEST_NAME, TEST_EMAIL)

        # Se o e-mail já existe (porque você já rodou esse teste antes),
        # não é um erro — só pulamos, já que a conta já está pronta pra uso.
        if register_page.is_visible(EMAIL_EXISTS_LOCATOR):
            pytest.skip(f"Conta {TEST_EMAIL} já existe — nada a fazer aqui.")

        register_page.fill_account_information(
            password=TEST_PASSWORD,
            first_name="Idna",
            last_name="Reis",
            address="Rua de Teste, 123",
            country="Brazil",
            state="Goias",
            city="Valparaiso de Goias",
            zipcode="72876000",
            mobile="11999999999",
        )

        assert register_page.is_account_created(), "A conta deveria ser criada com sucesso"
        register_page.continue_after_creation()
