# Employee API

A REST API for managing employee records built with Django and Django REST Framework.

## Requirements

- Python 3.8+
- pip

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Documentation

Interactive API documentation with request/response examples is available at:

**`http://localhost:8000/api/docs/`**

You can explore and test all endpoints directly from your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/employees/` | List all employees |
| POST | `/api/employees/` | Create a new employee |
| GET | `/api/employees/{id}/` | Retrieve a specific employee |
| DELETE | `/api/employees/{id}/` | Delete an employee |

### Employee Schema

```json
{
  "id": 1,
  "first_name": "Anna",
  "last_name": "Andersson",
  "email": "anna@example.com"
}
```

**Validation Rules:**
- `first_name` and `last_name`: Letters, spaces, hyphens, and apostrophes only (max 100 characters)
- `email`: Valid email format, must be unique (max 254 characters)

## Running Tests

```bash
python manage.py test
```

All tests should pass with 12 test cases covering validation, CRUD operations, and error handling.

## Design Notes

This implementation uses a repository pattern to abstract data access, making the codebase more maintainable and testable. Data is stored in-memory as specified in the requirements.
