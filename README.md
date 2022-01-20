# Template para projetos Django com Docker e PostgreSQL

Configurações iniciais para projetos Django, Docker e PosgtgreSQL (na porta 5433).

Pressupõe-se que o sistema operacional seja Linux

## Como utilizar

1. Clone do  repositório.
2. Entre na pasta
3. Execute o pre-build (copiar o .env e .env.db, se necessário, modifique as variáveis)
4. Execute o build
5. Execute as migrations
6. Carregue os usuários (usuário "admin@admin.com" e senha "admin")
7. Abra o navegador em http://127.0.0.1:8000/admin/

```console
git clone https://github.com/gguerran/django_docker_template.git
cd django_docker_template
make prebuild
make build
make migrate
make load_user_data
```

Comandos pre-configurados no Makefile:

Teste: 

`make test`

Remover containers:

`make down`

Remover containers com volumes

`make down_db`

Backup em arquivo json do banco:

`make dump_all`

Backup em arquivo json apenas dos usuários:

`make dump_users`

Comando migrate:

`make migrate`

Comando makemigrations:

`make makemigrations`

Reiniciar todas as migrations:

`make reset_migrations`

Apagar todas as pastas pycache:

`make delete_pycache`

Carregar todas as fixtures (arquivos json com dados do banco):

`make load_data`

Carregar apenas os dados de usuários:

`make load_user_data`

Subir o container:

`make up`

Verificar logs django (por padrão, o container roda em modo deatach)

`make logs`

Reformatar código pelo black e verificar o lint pelo flake8

`make lint`
