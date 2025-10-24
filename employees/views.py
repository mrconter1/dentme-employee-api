from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .repositories import repository
from .serializers import EmployeeSerializer


@extend_schema(responses=EmployeeSerializer(many=True))
@extend_schema(request=EmployeeSerializer, responses={201: EmployeeSerializer}, methods=['POST'])
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


@extend_schema(responses={200: EmployeeSerializer, 404: None})
@extend_schema(request=EmployeeSerializer, responses={200: EmployeeSerializer, 404: None}, methods=['PUT'])
@extend_schema(responses={204: None, 404: None}, methods=['DELETE'])
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, employee_id):
    if request.method == 'GET':
        employee = repository.get_employee(employee_id)
        if employee:
            return Response(employee)
        else:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )
    
    elif request.method == 'PUT':
        employee = repository.get_employee(employee_id)
        if not employee:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Pass instance to signal this is an update (used in email validation to exclude current employee)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            updated_employee = repository.update_employee(employee_id, **serializer.validated_data)
            return Response(updated_employee)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if repository.delete_employee(employee_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )

