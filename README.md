
🏛️ GovChain – Sistema de Emissão e Validação de Credenciais com Blockchain
GovChain é uma plataforma web desenvolvida para emissão, gerenciamento e verificação de credenciais digitais, com foco em segurança, rastreabilidade e transparência. O projeto foi idealizado como parte de uma iniciativa educacional para explorar tecnologias como Django REST Framework, controle de acesso por níveis de usuário e integração com blockchain.

🎯 Objetivo
Oferecer uma API robusta e segura para instituições emissoras de credenciais (como universidades, órgãos públicos ou empresas) e permitir que usuários consultem, validem e acompanhem suas credenciais digitais com confiabilidade, utilizando blockchain para garantir a integridade dos dados.

🚀 Funcionalidades

- 🔐 Autenticação com controle de permissões (3 níveis de acesso: Leitor, Emissor, Administrador)
  
- 🧾 CRUD completo para:
  - Subjects (titulares das credenciais)
  - Issuers (entidades emissoras)
  - Credentials (credenciais emitidas)
   
- 🔗 Geração de hash e registro em blockchain (na branch feature/blockchain-frontend)
  
- 📊 Dashboard web com Django Templates (na branch feature/blockchain-frontend)
  
- 📄 Documentação automática da API com Swagger/DRF Docs
  
- 🔍 Rotas de relacionamento:
  - /issuers/{id}/credentials/
  - /subjects/{id}/credentials/
  - /credentials/{id}/dashboard/

💻 Tecnologias Utilizadas
A aplicação foi construída com uma arquitetura moderna, separando as responsabilidades entre o front-end (navegador), o back-end (servidor) e o banco de dados.

Front-end (Interface do Usuário):

HTML5: Para a estruturação semântica do conteúdo.
CSS3: Para toda a estilização, animações e o design responsivo.
JavaScript (Vanilla): Para a interatividade da página, manipulação do DOM e consumo da API do back-end em tempo real via fetch.
Back-end (Lógica do Servidor):

Python 3: Linguagem principal para toda a lógica da aplicação.
Flask: Um micro-framework leve e poderoso para criar o servidor web e a API REST que gerencia usuários, comentários e o acesso ao banco de dados.
Werkzeug: Para gerar e verificar hashes de senhas, garantindo a segurança das contas dos usuários.
Banco de Dados:

MySQL: Um robusto sistema de gerenciamento de banco de dados relacional para armazenar os dados dos usuários, comentários e estoque de sangue.
MySQL Workbench: Ferramenta utilizada para modelar e administrar o banco de dados. 

🏛️ GovChain – Sistema de Emissão e Validação de Credenciais com Blockchain

👁️ Visão Geral

GovChain é uma API desenvolvida com Django REST Framework para emissão, gerenciamento e verificação de credenciais digitais. O sistema permite que instituições emissores criem credenciais para titulares, com rastreabilidade garantida por hash e estrutura de blocos. O projeto também implementa autenticação com controle de acesso por grupos (viewer, issuer, admin).

📦 Pacotes Utilizados

Pacote

Versão

Descrição

Django

= 5.0

Framework web principal

djangorestframework

latest

Toolkit para construção de APIs REST

django-environ

latest

Gerenciamento de variáveis de ambiente

drf-yasg

latest

Geração automática de documentação Swagger

Pillow

latest

Manipulação de imagens (se aplicável)

Consulte o arquivo requirements.txt para a lista completa e versões exatas.

🗂️ Estrutura do Projeto

govchain/
├── manage.py
├── requirements.txt
├── .env.example
├── govchain_id/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── credentials/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── utils/
│       └── blockchain.py
├── scripts/
│   └── setup_roles.py
└── docs/
    └── der_diagram.png

govchain_id/: configurações principais do projeto Django.

credentials/: app principal com modelos, views, serializers e lógica de blockchain.

scripts/: comandos customizados para setup automático de grupos e usuários.

docs/: diagramas e documentação visual.

🧩 Diagrama de Banco de Dados

O sistema possui três entidades principais:

Issuer: entidade emissora da credencial.

Subject: titular da credencial.

Credential: credencial emitida, vinculada a um issuer e subject.



📑 Documentação da API

A documentação interativa está disponível em:

/api/docs/ (Swagger UI)

/api/redoc/ (ReDoc)

Endpoints Principais

Método

Endpoint

Descrição

Autenticação

GET

/api/credentials/

Lista todas as credenciais

Requerida

POST

/api/credentials/

Cria uma nova credencial

Requerida

GET

/api/subjects/{id}/credentials/

Lista credenciais de um subject

Requerida

GET

/api/issuers/{id}/credentials/

Lista credenciais de um issuer

Requerida

⚙️ Configuração do Ambiente

# Clone o repositório
git clone https://github.com/Oliver4i2/govchain.git
cd govchain

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env  # Edite com suas credenciais

# Aplique migrações e configure grupos
python manage.py migrate
python manage.py setup_roles

# Inicie o servidor
python manage.py runserver

🚀 Deploy (opcional)

Plataformas recomendadas: Render, Railway, AWS

Prepare o Procfile:

web: gunicorn govchain_id.wsgi:application --log-file -

Configure variáveis de ambiente na plataforma

Execute migrações:

python manage.py migrate

Colete arquivos estáticos:

python manage.py collectstatic








