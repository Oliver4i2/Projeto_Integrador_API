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
| **Issuers** | `GET /api/issuers/, POST /api/issuers/` | Lista emissores, Cria novo emissor. |
| **Subjects** | `GET /api/subjects/, POST /api/subjects/` | Lista titulares, Cria novo titular. |
| **Credentials** | `GET /api/credentials/, POST /api/credentials/` | Lista credenciais, Cria nova credencial. |

## 🧪 Exemplos de Uso (cURL)
➡️ Criar Emissor
```bash
curl -X POST [http://127.0.0.1:8000/api/issuers/](http://127.0.0.1:8000/api/issuers/) \
-H "Content-Type: application/json" \
-d '{"name": "Universidade X", "did": "did:example:issuer1"}'
```
➡️ Criar Titular
```bash
curl -X POST [http://127.0.0.1:8000/api/subjects/](http://127.0.0.1:8000/api/subjects/) \
-H "Content-Type: application/json" \
-d '{"name": "Pedro", "did": "did:example:subject1"}'
```
➡️ Emitir Credencial
```bash
curl -X POST [http://127.0.0.1:8000/api/credentials/](http://127.0.0.1:8000/api/credentials/) \
-H "Content-Type: application/json" \
-d '{
  "issuer": 1,
  "subject": 1,
  "type": "Diploma",
  "data": {"curso": "Engenharia", "ano": 2025},
  "hash": "abc123..."
}'
```
## 📑 Documentação
Acesse as rotas abaixo com o servidor rodando para visualizar a documentação interativa:

Swagger UI: http://127.0.0.1:8000/api/docs/

OpenAPI Schema: http://127.0.0.1:8000/api/schema/

🔒 Autenticação
Por padrão, os endpoints exigem login. Para fins de desenvolvimento, você pode alterar as permissões no settings.py:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}
```
Nota: Em ambiente de produção, recomenda-se fortemente o uso de JWT ou OAuth2.

## 📌 Roadmap
[x] CRUD de emissores, titulares e credenciais

[x] Integração com blockchain para registro de hash

[x] Documentação Swagger

[ ] Implementar autenticação JWT

[ ] Dashboard com estatísticas avançadas
