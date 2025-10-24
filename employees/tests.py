from rest_framework.test import APITestCase
from rest_framework import status
from .repositories import repository


class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        repository.reset()

    def test_cannot_add_employee_with_duplicate_email(self):
        employee_data = {
            "first_name": "Anna",
            "last_name": "Andersson",
            "email": "anna@example.com"
        }
        
        response = self.client.post('/api/employees/', employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.post('/api/employees/', employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertIn('email', response.data['error'].lower())

