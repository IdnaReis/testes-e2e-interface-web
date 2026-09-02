"""
Dados fixos da conta de teste usada por login e checkout.

IMPORTANTE:
1. Rode `python -m pytest tests/test_cadastro.py -v -s` UMA VEZ para criar
   essa conta no site.
2. Depois disso, os testes de login e checkout vão reutilizar sempre a
   mesma conta abaixo. Não precisa rodar o cadastro de novo.
"""

TEST_EMAIL = "idnareis.qa.teste@exemplo.com"
TEST_PASSWORD = "SenhaForte123"
TEST_NAME = "Idna Teste"
