web: gunicorn libraryproject.wsgi
web: python manage.py migrate && python manage.py createsuperuser --noinput && gunicorn libraryproject.wsgi