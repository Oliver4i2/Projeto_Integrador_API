

O GovChain ID é uma plataforma para emissão e verificação de credenciais digitais verificáveis, integrando Django REST Framework com blockchain para garantir autenticidade, integridade e transparência.

Esta branch (feature/blockchain-frontend) adiciona:

Endpoints REST para emissores, titulares e credenciais.

Integração com blockchain para registrar e validar credenciais.

Documentação automática via Swagger/OpenAPI (/api/docs/).

🏗️ Arquitetura do Banco de Dados

Issuer → Emissor da credencial (ex.: universidade, órgão público).

Subject → Titular da credencial (ex.: estudante, cidadão).

Credential → Credencial digital verificável, vinculando Issuer ↔ Subject.

Relacionamentos:

Issuer (1:N) Credential (N:1) Subject

⚙️ Setup do Projeto

1. Clonar repositório

git clone <repo-url>
cd govchain_id
git checkout feature/blockchain-frontend

2. Instalar dependências

pip install -r requirements.txt

3. Aplicar migrations

python manage.py migrate

4. Criar superusuário

python manage.py createsuperuser

5. Rodar servidor

python manage.py runserver

🌐 Endpoints Principais

🔹 Issuers

GET /api/issuers/ → lista emissores

POST /api/issuers/ → cria emissor

🔹 Subjects

GET /api/subjects/ → lista titulares

POST /api/subjects/ → cria titular

🔹 Credentials

GET /api/credentials/ → lista credenciais

POST /api/credentials/ → cria credencial

🧪 Exemplos de Uso

➡️ Criar Emissor

curl -X POST http://127.0.0.1:8000/api/issuers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Universidade X", "did": "did:example:issuer1"}'

➡️ Criar Titular

curl -X POST http://127.0.0.1:8000/api/subjects/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Pedro", "did": "did:example:subject1"}'

➡️ Emitir Credencial

curl -X POST http://127.0.0.1:8000/api/credentials/ \
  -H "Content-Type: application/json" \
  -d '{
    "issuer": 1,
    "subject": 1,
    "type": "Diploma",
    "data": {"curso": "Engenharia", "ano": 2025},
    "hash": "abc123..."
  }'

📑 Documentação

Swagger UI: http://127.0.0.1:8000/api/docs/

OpenAPI Schema: http://127.0.0.1:8000/api/schema/

🔒 Autenticação

Por padrão, os endpoints exigem login.

Para desenvolvimento, pode-se usar:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny']
}

Em produção, recomenda-se JWT ou OAuth2.

📌 Roadmap

[x] CRUD de emissores, titulares e credenciais

[x] Integração com blockchain para registro de hash

[x] Documentação Swagger

[ ] Implementar autenticação JWT

[ ] Dashboard com estatísticas avançadas

👉 Esse README já está pronto para ser adicionado ao repositório.

Quer que eu já te monte o comando Git para salvar esse README.md na branch feature/blockchain-frontend e commitar direto?
