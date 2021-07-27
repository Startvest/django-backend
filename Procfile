release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py createsuperuser
web: gunicorn startvest_api.wsgi --log-file -