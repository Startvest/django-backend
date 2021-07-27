release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn startvest_api.wsgi --log-file -