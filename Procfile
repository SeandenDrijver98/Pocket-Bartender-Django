release: python manage.py migrate --noinput
web: gunicorn bartender_backend.wsgi --log-file -
worker: celery -A bartender_backend worker -l info
