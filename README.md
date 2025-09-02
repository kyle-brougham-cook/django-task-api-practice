# Django Task API (Practice Project)

A practice REST API built with Django REST Framework.  
Supports CRUD operations for tasks, with filtering and search functionality.

## Features

- List and create tasks (`ListCreateAPIView`)
- Retrieve, update, and delete tasks (`RetrieveUpdateDestroyAPIView`)
- Query params for:
  - `?d=true/false` → filter by done status
  - `?q=search-term` → search by title or description

## Tech Stack

- Python 3
- Django 5
- Django REST Framework

## Setup

```bash
git clone <repo-url>
cd django-task-api-practice.taskManager
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
python manage.py runserver
```
