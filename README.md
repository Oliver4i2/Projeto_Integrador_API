
# 🏛️ GovChain

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![DRF](https://img.shields.io/badge/DRF-Latest-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Sistema de Emissão e Validação de Credenciais com Blockchain**

## 👁️ Visão Geral

O **GovChain** é uma API robusta desenvolvida com **Django REST Framework** focada na emissão, gerenciamento e verificação de credenciais digitais. O diferencial do sistema é a implementação de uma estrutura lógica de **Blockchain**, garantindo a imutabilidade e rastreabilidade dos dados através de hashing e encadeamento de blocos.

Além disso, o projeto implementa um sistema de controle de acesso baseado em funções (RBAC) com grupos distintos: `viewer`, `issuer` e `admin`.

---

## 📑 Índice

- [📦 Pacotes e Tecnologias](#-pacotes-e-tecnologias)
- [🗂️ Estrutura do Projeto](#-estrutura-do-projeto)
- [🧩 Modelagem de Dados](#-modelagem-de-dados)
- [🔌 Endpoints da API](#-endpoints-da-api)
- [⚙️ Instalação e Configuração](#-instalação-e-configuração)
- [🚀 Deploy](#-deploy-opcional)

---

## 📦 Pacotes e Tecnologias

O projeto utiliza as seguintes bibliotecas principais:

| Pacote | Versão | Descrição |
| :--- | :---: | :--- |
| **Django** | `5.0` | Framework web principal de alto nível. |
| **Django REST Framework** | `Latest` | Toolkit poderoso para construção de APIs Web. |
| **django-cors-headers** | `Latest` | GPermite requisições cross-origin (CORS), útil para integração com front-end. |
| **drf-yasg** | `Latest` | Geração automática de documentação Swagger/Redoc. |
| **python-decouple** | `Latest` | Gerenciamento de variáveis de ambiente via .env . |
| **PyJWT** | `Latest` | Geração e verificação de tokens JWT para autenticação. |
| **bcrypt** | `Latest` | Hashing de senhas seguro (opcional, se usado no projeto). |

> *Consulte o arquivo `requirements.txt` para a lista completa de dependências.*

---

## 🗂️ Estrutura do Projeto

Abaixo está a árvore de diretórios principal do sistema:

```text
govchain/
├── manage.py                   # Utilitário de linha de comando do Django
├── requirements.txt            # Dependências do projeto
├── .env.example                # Modelo de variáveis de ambiente
├── govchain_id/                # Configurações do projeto (Settings, URLS)
│   ├── settings.py
│   └── urls.py
├── credentials/                # Aplicação Principal
│   ├── models.py               # Modelos (Issuer, Subject, Credential)
│   ├── views.py                # Lógica dos endpoints
│   ├── serializers.py          # Serialização de dados
│   └── utils/
│       └── blockchain.py       # Lógica de Hashing e validação de blocos
├── scripts/
│   └── setup_roles.py          # Script para criação automática de grupos/permissões
└── docs/                       # Documentação estática e diagramas
```
## 🧩 Banco de Dados
<img width="1024" height="1024" alt="Entity-Relationship " src="https://github.com/user-attachments/assets/62ff6b92-8eb5-4daf-93c6-95ad867ab97c" />

1. Issuer (Emissor)
Função: Representa a instituição ou entidade responsável por emitir credenciais.

Campos críticos:

id: chave primária única.

name: nome da instituição emissora.

did: identificador descentralizado (Decentralized Identifier), usado para garantir autenticidade.

Observação: Um emissor pode emitir várias credenciais.

2. Subject (Titular)
Função: Representa o indivíduo ou organização que recebe a credencial.

Campos críticos:

id: chave primária única.

name: nome do titular.

did: identificador descentralizado, garantindo unicidade e rastreabilidade.

Observação: Um titular pode receber várias credenciais.

3. Credential (Credencial)
Função: Documento digital emitido pelo Issuer e vinculado a um Subject.

Campos críticos:

id: chave primária única.

issuer_id: chave estrangeira que referencia o emissor.

subject_did: chave estrangeira que referencia o titular.

type: tipo da credencial (ex: diploma, certificado, identidade).

data: informações específicas da credencial (JSON ou texto estruturado).

hash: valor criptográfico que garante integridade e imutabilidade.

timestamp: data/hora da emissão.

Observação: É a entidade central do sistema, conectando Issuer e Subject.

🔗 Relacionamentos
Issuer → Credential:

Tipo: 1:N

Descrição: Um emissor pode emitir várias credenciais, mas cada credencial pertence a apenas um emissor.

Subject → Credential:

Tipo: 1:N

Descrição: Um titular pode receber várias credenciais, mas cada credencial pertence a apenas um titular.

⚠️ Campos Críticos para Segurança
did (Issuer e Subject): garante unicidade e autenticidade dos atores.

hash (Credential): protege contra adulteração e assegura integridade dos dados.

timestamp (Credential): registra o momento da emissão, essencial para auditoria e rastreabilidade.
-----

## 🔌 Endpoints da API

A documentação interativa completa (Swagger UI) está disponível em `/api/docs/` ou `/api/redoc/` após iniciar o servidor.

-----

### Principais Rotas

| Método | Endpoint | Descrição | Autenticação |
| :---: | :--- | :--- | :---: |
| `GET` | `/api/credentials/` | Lista todas as credenciais registradas. | 🔒 Sim |
| `POST` | `/api/credentials/` | Emite uma nova credencial (Gera Hash/Bloco). | 🔒 Sim |
| `GET` | `/api/subjects/{id}/credentials/` | Lista histórico de credenciais de um titular. | 🔒 Sim |
| `GET` | `/api/issuers/{id}/credentials/` | Lista credenciais emitidas por uma instituição. | 🔒 Sim |

-----

⚙️ Instalação e Configuração
Siga os passos abaixo para configurar e rodar o projeto localmente.
-----
1. Clone o repositório
Bash
```
git clone [https://github.com/Oliver4i2/govchain.git](https://github.com/Oliver4i2/govchain.git)
cd govchain
```
-----
2. Crie o Ambiente Virtual
Bash
```
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate
```
-----
3. Instale as Dependências
Bash
```
pip install -r requirements.txt
```
-----
4. Variáveis de Ambiente
Copie o arquivo de exemplo e configure suas credenciais (Secret Key, Debug, Banco de Dados):
Bash
```
cp .env.example .env
```
-----
5. Banco de Dados e Permissões
Aplique as migrações e execute o script customizado para criar os grupos de acesso iniciais:
Bash
```
python manage.py migrate
python manage.py setup_roles
```
-----
6. Inicie o Servidor
Bash
```
python manage.py runserver
```
-----
Acesse em: http://127.0.0.1:8000/

-----
🚀 Deploy (Opcional)
O projeto está configurado para facilitar o deploy em plataformas como Render, Railway ou AWS.

Configuração do Procfile (Gunicorn)
Plaintext
```
web: gunicorn govchain_id.wsgi:application --log-file -
```
-----
Passos pós-deploy
Configure as variáveis de ambiente no painel da sua hospedagem.

Execute as migrações e a coleta de arquivos estáticos:
Bash
```
python manage.py migrate
python manage.py collectstatic
```
-----








