# Personal Finance

This a simple personal finance application that allows users to track their expenses and income. The application is built using Python and FastAPI.

# Architecture

The application dont follow any specific architecture, but it is divided into the following components:
- entities
- controllers
- services
- repositories
- routes
- presenters

## Tools
- Python 3.13.2
- FastAPI

## Installation
1. Clone the repository
2. Create a virtual environment using `python -m venv .venv .venv\Scripts\activate` (windows)
3. Install the dependencies using `pip install -r requirements.txt`
4. Run the application using `fastapi dev .\src\main.py`

## Documentation
1. Open the browser and navigate to:
- [Swagger](http://127.0.0.1:8000/docs#/)
- [Redoc](http://127.0.0.1:8000/redoc#tag/)

## Requisitos

Para desenvolver um sistema de controle financeiro eficaz, é importante considerar funcionalidades como:

- Controle de contas: Permitir o gerenciamento de múltiplas contas bancárias com a possibilidade de cadastrar saldos iniciais.
- Registro de receitas e despesas: Facilitar o lançamento de entradas e saídas financeiras, categorizando-as adequadamente.
- Conciliação bancária: Integrar-se com bancos para importar extratos e realizar a conciliação manual.
- Geração de relatórios financeiros: Produzir relatórios detalhados sobre a saúde financeira, ajudando na tomada de decisão.
- Segurança e backup de dados: Garantir a proteção e integridade das informações financeiras.
