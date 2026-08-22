# 📡 NetDevOps Portal – Provisionamento Remoto de Redes

Aplicação Web em Python para automação e gerenciamento de infraestruturas de rede (Cisco, Mikrotik e Huawei). Desenvolvida para integrar conceitos de redes IP e desenvolvimento back-end.

## 🎯 Funcionalidades
* **Credenciais Dinâmicas:** Acesso dinâmico via SSH sem expor senhas no código.
* **Multi-Vendor:** Suporte automatizado a comandos para Cisco IOS, Mikrotik RouterOS e Huawei VRP.
* **Tratamento de Exceções de Rede:** Identificação de falhas de autenticação e timeout de conexão.

## 🛠️ Tecnologias Utilizadas
* **Back-end:** Python 3.11, Flask, Netmiko (Paramiko/SSH)
* **Front-end:** HTML5, CSS3
* **Sistema Operacional de Desenvolvimento:** Linux (Keep-OS / Ubuntu)

## 🔧 Como Executar Localmente
1. Clone o repositório:
    bash
    git clone https://github.com/SEU_USUARIO/telecom-netdevops-dashboard.git
    cd telecom-netdevops-dashboard
2. Crie e ative o ambiente virtual:
    bash
    python3 -m venv .venv
    source .venv/bin/activate
3. Instale as dependências:
    bash
    pip install -r requirements.txt
4. Execute o servidor Flask:
    bash
    python app.py
5. Acesse `http://127.0.0.1:5000` no navegador.
---