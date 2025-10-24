from rest_framework.decorators import api_view
from rest_framework.response import Response
from .repositories import repository


@api_view(['GET'])
def list_employees(request):
    employees = repository.get_all_employees()
    return Response(employees)

