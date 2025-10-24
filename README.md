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

**POST /api/employees/** - Add a new employee. Required fields: first_name, last_name, email (must be unique).

**DELETE /api/employees/{id}/** - Delete an employee by ID.

## Running Tests

```bash
python manage.py test
```

