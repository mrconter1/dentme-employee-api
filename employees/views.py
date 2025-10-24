from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .repositories import repository
from .serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
def list_employees(request):
    if request.method == 'GET':
        employees = repository.get_all_employees()
        return Response(employees)
    
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = repository.add_employee(**serializer.validated_data)
            return Response(employee, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_employee(request, employee_id):
    if repository.delete_employee(employee_id):
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(
            {"error": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )

