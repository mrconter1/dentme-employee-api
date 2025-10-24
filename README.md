# Employee API

A REST API for managing employee records built with Django and Django REST Framework.

## Requirements

Python 3.8+ and pip.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Employee Model

Each employee has an id (auto-generated), first_name, last_name, and email (unique).

## API Endpoints

**GET /api/employees/** - List all employees.

## Running Tests

```bash
python manage.py test
```

