release: python manage.py migrate --noinput
web: gunicorn gosasa_tracker.wsgi --log-file -
worker: celery -A bartender_backend worker -l info
