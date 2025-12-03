# Hospital Management System - Deployment Guide

## Project Overview

Django-based Hospital Management System with Patient, Doctor, and Appointment models.

### Key Features
- Patient Management
- Doctor Management
- Appointment Scheduling
- Django Admin Interface
- Responsive Web Interface

## Current Status

### Completed
✅ Django application development
✅ Database models (Patient, Doctor, Appointment)
✅ Admin interface configuration
✅ GitHub repository setup
✅ Render deployment (home page working)
✅ Procfile.prod created for Railway
✅ settings.py configured for production

### Admin Credentials
- **Username**: mustafa
- **Password**: mustafa123@
- **Email**: mustafa123@

## Deployment Options

### Option 1: Railway (Recommended)
Railway provides better support for Django with built-in database migrations.

**Advantages:**
- Supports release phases for migrations
- Better Python support
- Easier scaling
- Good free tier

**Steps:**
1. Go to railway.app
2. Click "Create Project"
3. Select "Deploy from GitHub"
4. Authorize Railway app with GitHub
5. Select GEEDDIGA/hospital- repository
6. Railway will auto-detect Django and use Procfile.prod
7. Set ALLOWED_HOSTS environment variable

**Environment Variables:**
```
ALLOWED_HOSTS=<your-railway-domain>.railway.app
DEBUG=False
```

### Option 2: Render (Currently Active)
Render is a great free tier platform but has limitations with free tier pre-deploy commands.

**Current Issue:**
- Free tier doesn't support Pre-Deploy Commands
- Database migrations must run as part of the build command
- Currently configured to run migrations in Build Command

**Build Command:**
```
pip install -r requirements.txt && python manage.py migrate
```

**Current Render URL:**
https://hospital-app-zkm0.onrender.com/

**Workaround for admin access:**
Use SSH access through Render Shell:
```
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_superuser('mustafa', 'mustafa123@', 'mustafa123@')
```

### Option 3: Heroku (Legacy)
Note: Heroku free tier was discontinued in November 2022.

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Files Included

- `Procfile` - Heroku/Render deployment configuration
- `Procfile.prod` - Railway deployment configuration with migration support
- `requirements.txt` - Python dependencies
- `hospital/settings.py` - Django configuration with ALLOWED_HOSTS
- `render-build.sh` - Render-specific build script

## Troubleshooting

### Admin interface returns 500 error
**Cause:** Database tables don't exist
**Solution:** 
- For Railway: Run via release command (automatic)
- For Render: Use Shell or update Build Command
- For local: Run `python manage.py migrate`

### ALLOWED_HOSTS configuration error
**Solution:** Update the domain in settings.py or environment variables

### Static files not loading
**Solution:** Run `python manage.py collectstatic`

## Next Steps

1. **Complete Railway Deployment:**
   - Install Railway CLI or use web dashboard
   - Connect GitHub repository
   - Set environment variables
   - Test admin interface

2. **Enhance Production Deployment:**
   - Set up PostgreSQL instead of SQLite
   - Configure static file storage
   - Set up SSL certificates
   - Configure email backend

3. **Security Improvements:**
   - Review SECURITY settings
   - Enable CSRF protection
   - Configure CORS headers
   - Use environment variables for secrets

## Support

For issues or questions, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Railway Docs: https://docs.railway.app/
- Render Docs: https://render.com/docs
