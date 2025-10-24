from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .repositories import repository


@api_view(['GET', 'POST'])
def list_employees(request):
    if request.method == 'GET':
        employees = repository.get_all_employees()
        return Response(employees)
    
    elif request.method == 'POST':
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        
        if not first_name or not last_name or not email:
            return Response(
                {"error": "first_name, last_name, and email are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if repository.email_exists(email):
            return Response(
                {"error": "An employee with this email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        employee = repository.add_employee(first_name, last_name, email)
        return Response(employee, status=status.HTTP_201_CREATED)

