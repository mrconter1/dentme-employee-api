from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.list_employees),
    path('employees/<int:employee_id>/', views.employee_detail),
]

