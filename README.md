# Employee API

A REST API for managing employee records built with Django and Django REST Framework.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Design Decisions](#design-decisions)
- [Next Steps](#next-steps)

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

The API will be available at `http://localhost:8000/api/v1/`

## API Documentation

Interactive API documentation with request/response examples is available at:

**`http://localhost:8000/api/docs/`**

You can explore and test all endpoints directly from your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/employees/` | List all employees |
| POST | `/api/v1/employees/` | Create a new employee |
| GET | `/api/v1/employees/{id}/` | Retrieve a specific employee |
| PUT | `/api/v1/employees/{id}/` | Update an employee |
| DELETE | `/api/v1/employees/{id}/` | Delete an employee |

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

All tests should pass with 14 test cases covering validation, CRUD operations, and error handling.

## Design Decisions

- I consciously added two operations beyond the three required to follow standard **CRUD** conventions and make the API more complete.
- I chose the **repository pattern** to allow for easy swapping of backend storage, making it simple to migrate from in-memory to PostgreSQL without touching views or serializers.
- I chose **Django** REST Framework partly because most APIs work similarly but also because that is what Dentme currently uses.
- I added **API versioning** (`/api/v1/`) to make it more proper and maintainable. Should have added this earlier as it became a large git diff when fixing it later.
- I consciously chose not to use Django ORM for this task as it felt like over-engineering given the requirements.

## Next Steps

- **API authentication**: would be relatively easy to add and would be needed before we deploy.
- **Production deployment**: would require disabling DEBUG variable, proper environment configuration, and setting up CI/CD.
- **Django ORM**: natural next step for code elegance, readability, and persistence.
- **Pagination**: would almost be needed from the moment we deploy, especially for the get all employees endpoint.
- **Connect a simple front-end**: build something quick for end users that could further validate behavior.
