🧪 Testes de ponta a ponta (E2E) — Interface Web

> Automação de fluxos completos de usuário simulando comportamento real em uma aplicação web.

## 📋 Sobre o Projeto

Este projeto demonstra a criação de Testes End-to-End (E2E), cobrindo os fluxos principais de uma aplicação web de e-commerce ([automationexercise.com](https://automationexercise.com), site público para prática de QA):

- 🔒 **Login** — Acesso do usuário (com credenciais válidas e inválidas)
- 📝 **Cadastro** — Registro de novo usuário
- 🛒 **Checkout** — Finalização de compra

O objetivo é simular exatamente o caminho que um usuário real faria na plataforma, validando cada etapa do início ao fim.

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Descrição |
|---|---|
| 🐍 Python | Linguagem de programação |
| 🌐 Selenium | Automação de navegador |
| ✅ Pytest | Framework de testes |
| 📄 pytest-html | Relatórios em HTML |
| 🔧 webdriver-manager | Gerencia o driver do Chrome automaticamente |

## 📂 Estrutura do Projeto

```
e2e-tests-portfolio/
├── pages/                  # Page Object Model (uma classe por tela)
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   └── checkout_page.py
├── tests/                  # Casos de teste
│   ├── test_login.py
│   ├── test_cadastro.py
│   └── test_checkout.py
├── conftest.py             # Configuração do driver + captura de screenshots
├── pytest.ini              # Configuração do pytest e do relatório HTML
├── requirements.txt
└── reports/                # Relatório HTML gerado após a execução
```

## ▶️ Como Executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ajuste os dados de teste** (opcional, mas recomendado):
   - Em `tests/test_login.py` e `tests/test_checkout.py`, troque `VALID_EMAIL` / `EMAIL` e `PASSWORD` por uma conta real criada no site (você pode rodar `test_cadastro.py` primeiro para criar uma).

3. **Rode os testes:**
   ```bash
   pytest
   ```
   Isso já vai gerar automaticamente:
   - Um relatório HTML em `reports/report.html`
   - Screenshots de cada teste (passou ou falhou) em `screenshots/`

4. **Rode um arquivo específico:**
   ```bash
   pytest tests/test_cadastro.py -v
   ```

## 📊 Evidências

- **Relatório HTML**: `reports/report.html` — mostra o resultado de cada teste, tempo de execução e logs
- **Screenshots**: `screenshots/` — print da tela ao final de cada teste, nomeado com o resultado (ex: `test_login_com_credenciais_validas_PASSOU.png`)

## 🎯 Próximos passos

- Adicionar testes de regressão adicionais (ex: recuperação de senha, edição de perfil)
- Integrar com GitHub Actions para rodar os testes automaticamente a cada commit
- Adicionar testes de responsividade (mobile/desktop)

---
Desenvolvido por Idna Reis — [GitHub](https://github.com/IdnaReis) | [LinkedIn](https://linkedin.com/in/qaxia-tech).
