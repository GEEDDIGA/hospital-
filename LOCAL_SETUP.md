# Hospital Management System - Local Setup Guide

## Quick Start (5 minutes)

This guide will help you run the hospital management system locally.

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git
- A terminal/command prompt

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/GEEDDIGA/hospital-.git
cd hospital-
```

---

## Step 2: Create Virtual Environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Create .env File

Create `.env` in project root:

```
DEBUG=True
SECRET_KEY=django-insecure-local-development
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@hospital.com
ADMIN_PASSWORD=admin123
```

---

## Step 5: Run Migrations

```bash
python manage.py migrate
```

---

## Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Username: admin
Email: admin@hospital.com
Password: admin123

---

## Step 7: Start Development Server

```bash
python manage.py runserver
```

App available at: http://127.0.0.1:8000/

---

## Step 8: Access Admin

Go to: http://127.0.0.1:8000/admin/
Login: admin / admin123

---

## Using VS Code Server

1. Install VS Code Server
2. Open project folder
3. Open integrated terminal (Ctrl + `)
4. Follow steps 2-7 above
5. VS Code will show server preview link

---

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Reset Database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Deactivate Virtual Environment
```bash
deactivate
```

---

## Key Technologies

- Django 4.2.5
- Django REST Framework 3.14.0
- Celery 5.3.4
- Pytest 7.4.3
- Gunicorn 20.0.4

---

**App Ready! Start Developing!**
