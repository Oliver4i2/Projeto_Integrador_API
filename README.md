# 📖 GovChain ID

## 🚀 Visão Geral
O **GovChain ID** é uma plataforma para emissão e verificação de credenciais digitais verificáveis, integrando **Django REST Framework** com **blockchain** para garantir autenticidade, integridade e transparência.

Esta branch (`feature/blockchain-frontend`) adiciona:
* **Endpoints REST** para emissores, titulares e credenciais.
* **Integração com blockchain** para registrar e validar credenciais.
* **Documentação automática** via Swagger/OpenAPI (`/api/docs/`).

---

## 🏗️ Arquitetura do Banco de Dados
A estrutura de dados é baseada em três pilares principais:

* **Issuer**: Emissor da credencial (ex.: universidade, órgão público).
* **Subject**: Titular da credencial (ex.: estudante, cidadão).
* **Credential**: Credencial digital verificável, vinculando `Issuer` ↔ `Subject`.

### Relacionamentos:
`Issuer (1:N) <---> Credential <---> (N:1) Subject`

---

## ⚙️ Setup do Projeto

### 1. Clonar repositório
```bash
git clone [https://github.com/seu-usuario/govchain_id.git](https://github.com/seu-usuario/govchain_id.git)
cd govchain_id
git checkout feature/blockchain-frontend
```

## 2. Instalar dependências
```bash
pip install -r requirements.txt
```
## 3. Aplicar migrations
```bash
python manage.py migrate
```
## 4. Criar superusuário (Admin)
```bash
python manage.py createsuperuser
```
## 5. Rodar servidor
```bash
python manage.py runserver
```
## 🌐 Endpoints Principais
| Recurso | Endpoint | Descrição |
| :--- | :---: | :--- |
| **Issuers** | `GET /api/issuers/,POST /api/issuers/` | Framework web principal de alto nível. |
| **Django REST Framework** | `Latest` | Toolkit poderoso para construção de APIs Web. |
| **django-cors-headers** | `Latest` | GPermite requisições cross-origin (CORS), útil para integração com front-end. |
| **drf-yasg** | `Latest` | Geração automática de documentação Swagger/Redoc. |
| **python-decouple** | `Latest` | Gerenciamento de variáveis de ambiente via .env . |
| **PyJWT** | `Latest` | Geração e verificação de tokens JWT para autenticação. |
| **bcrypt** | `Latest` | Hashing de senhas seguro (opcional, se usado no projeto). |
