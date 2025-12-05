web: gunicorn hospital.wsgi --log-file -
release: python manage.py migrate && python build-db.py
