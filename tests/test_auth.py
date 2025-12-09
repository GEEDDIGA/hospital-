import pytest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class AdminLoginTest(TestCase):
    """Test Django admin login functionality"""
    
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@hospital.com',
            password='admin123'
        )
    
    def test_admin_login_page_accessible(self):
        """Test that admin login page is accessible"""
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log in', response.content)
    
    def test_admin_login_success(self):
        """Test successful admin login"""
        login_success = self.client.login(
            username='admin',
            password='admin123'
        )
        self.assertTrue(login_success)
    
    def test_admin_login_with_wrong_password(self):
        """Test admin login fails with wrong password"""
        login_success = self.client.login(
            username='admin',
            password='wrongpassword'
        )
        self.assertFalse(login_success)
    
    def test_admin_login_with_wrong_username(self):
        """Test admin login fails with wrong username"""
        login_success = self.client.login(
            username='nonexistent',
            password='admin123'
        )
        self.assertFalse(login_success)
    
    def test_admin_dashboard_accessible_after_login(self):
        """Test admin can access dashboard after login"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Django administration', response.content)
    
    def test_admin_dashboard_redirect_without_login(self):
        """Test unauthenticated user redirected from admin"""
        response = self.client.get('/admin/', follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)


class APIAuthenticationTest(TestCase):
    """Test API authentication and JWT tokens"""
    
    def setUp(self):
        self.api_client = APIClient()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@hospital.com',
            password='testpass123'
        )
    
    def test_api_requires_authentication(self):
        """Test API endpoints require authentication"""
        response = self.api_client.get('/api/patients/')
        self.assertIn(response.status_code, [401, 403])
    
    def test_authenticated_api_access(self):
        """Test authenticated user can access API"""
        self.api_client.force_authenticate(user=self.test_user)
        response = self.api_client.get('/api/patients/')
        self.assertEqual(response.status_code, 200)


class SessionManagementTest(TestCase):
    """Test session and logout functionality"""
    
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@hospital.com',
            password='admin123'
        )
    
    def test_session_created_after_login(self):
        """Test session is created after successful login"""
        self.client.login(username='admin', password='admin123')
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(
            int(self.client.session['_auth_user_id']),
            self.admin_user.pk
        )
    
    def test_logout_clears_session(self):
        """Test logout clears the session"""
        self.client.login(username='admin', password='admin123')
        self.assertIn('_auth_user_id', self.client.session)
        
        self.client.logout()
        self.assertNotIn('_auth_user_id', self.client.session)
