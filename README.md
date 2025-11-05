#  Projeto Cadastro de Usuários – Django + Django REST Framework

Este é um **projeto de aprendizado** desenvolvido com Django, que permite gerenciar usuários tanto através de uma **interface web tradicional** quanto de uma **API REST protegida com JWT**.  
O objetivo do projeto foi praticar conceitos de **CRUD, APIs e autenticação**
---

## 🚀 Funcionalidades

- Interface web para:
  - Listar usuários
  - Cadastrar novos usuários
  - Editar usuários existentes
  - Excluir usuários
- API REST para:
  - Listar usuários (`GET /api/usuarios/`)
  - Criar usuários (`POST /api/usuarios/`)
  - Atualizar e deletar usuários
- Autenticação JWT para proteger rotas da API

> ⚠️ Observação: Este projeto foi criado como estudo e prática com orientação de ferramentas de apoio.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**  
- **Django 5.2.7**  
- **Django REST Framework 3.16.1**  
- **djangorestframework_simplejwt 5.5.1**
- **SimpleJWT 2.10.1**  
- **psycopg2-binary 2.9.11** 
- **PostgreSQL**

---

## 📁 Estrutura do Projeto

cadastro_api/ # Projeto principal
│
├── cadastro_api/
│ ├── settings.py # Configurações do projeto
│ ├── urls.py # Rotas principais
│
├── usuario/ # App principal
│ ├── models.py # Modelos de dados
│ ├── views.py # Views para interface web
│ ├── views_api.py # Views para API REST
│ ├── serializers.py # Conversão entre JSON e Python
│ ├── urls.py # Rotas específicas da app
│
├── templates/ # HTML da interface web
├── manage.py
└── README.md

Instalação e Execução

1.Clone o repositório  
   ```bash
   git clone https://github.com/CelsiaJose/djangoapi.git
   cd djangoapi

2. Crie um ambiente virtual

python -m venv api1
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows

3.
pip install -r requirements.txt

Execute as migrações

python manage.py makemigrations
python manage.py migrate

4.Crie um superusuário

python manage.py createsuperuser

5.Rode o servidor

python manage.py runserver

6.Acessos 

Acesse a interface web em http://127.0.0.1:8000/
E a API em http://127.0.0.1:8000/api/usuarios/ 

🔮 Melhorias Futuras

Algumas ideias e aprimoramentos planejados para versões futuras do projeto:

✅ Implementar testes automatizados para as rotas da API

✅ Adicionar páginas de login e logout na interface web

✅ Criar validação de senha com requisitos mínimos de segurança

✅ Adicionar autenticação social (Google, GitHub, etc.)

✅ Implementar paginação e filtros nas listagens da API

✅ Adicionar documentação automática com Swagger ou Redoc

✅ Criar um frontend separado (React ou Vue) para consumir a API

✅ Implantar o projeto em um servidor (Render, Railway ou AWS)



Autora

Celsia Marta José
Desenvolvedora em formação | Backend com Django
📧 celsiasilvacs@gmail.com



