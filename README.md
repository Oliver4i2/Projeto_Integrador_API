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

2. Instalar dependências
Bash

pip install -r requirements.txt
3. Aplicar migrations
Bash

python manage.py migrate
4. Criar superusuário (Admin)
Bash

python manage.py createsuperuser
5. Rodar servidor
Bash

python manage.py runserver
