"""
Testes E2E — Fluxo de Checkout
Cobre: adicionar produto ao carrinho, ir para o carrinho, finalizar o pedido
e concluir o pagamento.

Usa a conta fixa definida em test_data.py — rode test_cadastro.py uma vez
antes, para garantir que essa conta exista no site.
"""
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from test_data import TEST_EMAIL, TEST_PASSWORD


class TestCheckout:

    def test_finalizar_compra_com_sucesso(self, driver):
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Login
        login_page.open_login()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)
        assert login_page.is_login_successful(), "É necessário estar logado para finalizar a compra"

        # 2. Adicionar produto ao carrinho
        checkout_page.add_first_product_to_cart()

        # 3. Ir para o carrinho e prosseguir
        checkout_page.go_to_cart()
        checkout_page.proceed_to_checkout()

        # 4. Confirmar pedido
        checkout_page.place_order(comment="Pedido de teste automatizado")

        # 5. Preencher pagamento (dados fictícios de teste)
        checkout_page.fill_payment_details(
            name_on_card="Idna Reis",
            card_number="4111111111111111",
            cvc="123",
            month="12",
            year="2030",
        )

        assert checkout_page.is_order_successful(), "O pedido deveria ser confirmado com sucesso"
