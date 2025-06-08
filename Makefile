run:
	python manage.py runserver

migrate:
	python manage.py makemigrations main_app
	python manage.py makemigrations
	python manage.py migrate

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

flush:
	python manage.py flush

admin:
	python manage.py createsuperuser
