shell:
    python manage.py shell

migrate:
    python manage.py migrate

makemigrations app:
    python manage.py makemigrations {{ app }}

runserver:
    python manage.py runserver

startapp app:
    python manage.py startapp {{ app }}

createsuperuser:
    python manage.py createsuperuser