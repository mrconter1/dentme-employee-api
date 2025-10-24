from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.list_employees),
]

