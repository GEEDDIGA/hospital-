web: gunicorn hospital.wsgi --log-file -
release: python manage.py migrate && python manage.py shell -c 'import os;os.environ.setdefault("DJANGO_SETTINGS_MODULE","hospital.settings");import django;django.setup();from django.contrib.auth.models import User;User.objects.filter(username="mustafa").delete();User.objects.create_superuser("mustafa","mustafa@example.com","mustafa123@")'
