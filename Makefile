prebuild:
	cp .env.example .env
	cp .db.env.example .db.env

build:
	docker-compose up -d --build

down_db:
	docker-compose down -v

down:
	docker-compose down

dump_all:
	docker-compose exec project_django python manage.py dumpdata --indent 4 \
	--exclude admin --exclude auth --exclude contenttypes --exclude sessions \
	--exclude messages --exclude staticfiles > fixtures/all_data.json

dump_users:
	docker-compose exec project_django python manage.py dumpdata --indent 4 accounts.User > fixtures/accounts_user.json

migrate:
	docker-compose exec project_django python manage.py migrate

makemigrations:
	docker-compose exec project_django python manage.py makemigrations

reset_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/venv/*" -delete
	docker-compose down -v
	docker-compose up -d
	docker-compose exec project_django python manage.py makemigrations
	docker-compose exec project_django python manage.py migrate
	docker-compose exec project_django python manage.py loaddata fixtures/all_data.json

delete_pycache:
	find . -path "*/__pycache__" | xargs rm -rf

load_data:
	docker-compose exec project_django python manage.py loaddata fixtures/*.json

load_user_data:
	docker-compose exec project_django python manage.py loaddata fixtures/accounts_user.json

test:
	docker-compose exec project_django python manage.py test

createsuperuser:
	docker-compose exec project_django python manage.py createsuperuser

up:
	docker-compose up -d

logs:
	docker logs project_django

lint:
	docker-compose exec project_django black .
	docker-compose exec project_django flake8 . --extend-exclude=migrations,venv --max-line-length 120
