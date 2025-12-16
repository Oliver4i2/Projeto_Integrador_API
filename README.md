
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








