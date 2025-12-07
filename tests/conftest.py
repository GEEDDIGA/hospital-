import os
import django
from django.conf import settings
import pytest
from django.test.utils import get_unique_databases_and_mirrors

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


@pytest.fixture(scope='session')
def django_db_setup():
    """Configure database for tests"""
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_hospital',
        'USER': 'test_user',
        'PASSWORD': 'test_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }


@pytest.fixture
def client():
    """Django test client fixture"""
    from django.test import Client
    return Client()


@pytest.fixture
def authenticated_client():
    """Authenticated Django test client"""
    from django.test import Client
    from django.contrib.auth.models import User
    
    client = Client()
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    client.login(username='testuser', password='testpass123')
    return client


@pytest.fixture
def api_client():
    """DRF API test client"""
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def authenticated_api_client():
    """Authenticated DRF API test client"""
    from rest_framework.test import APIClient
    from django.contrib.auth.models import User
    
    client = APIClient()
    user = User.objects.create_user(
        username='apiuser',
        email='api@example.com',
        password='apipass123'
    )
    client.force_authenticate(user=user)
    return client
