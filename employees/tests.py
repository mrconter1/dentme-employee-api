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
        self.assertIn('email', response.data)

    def test_add_two_employees_and_list_all(self):
        employee1 = {
            "first_name": "Anna",
            "last_name": "Andersson",
            "email": "anna@example.com"
        }
        employee2 = {
            "first_name": "Erik",
            "last_name": "Svensson",
            "email": "erik@example.com"
        }
        
        response1 = self.client.post('/api/employees/', employee1, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        
        response2 = self.client.post('/api/employees/', employee2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        self.assertEqual(response.data[0]['first_name'], 'Anna')
        self.assertEqual(response.data[0]['last_name'], 'Andersson')
        self.assertEqual(response.data[0]['email'], 'anna@example.com')
        self.assertEqual(response.data[0]['id'], 1)
        
        self.assertEqual(response.data[1]['first_name'], 'Erik')
        self.assertEqual(response.data[1]['last_name'], 'Svensson')
        self.assertEqual(response.data[1]['email'], 'erik@example.com')
        self.assertEqual(response.data[1]['id'], 2)

    def test_can_add_employees_with_same_name_but_different_email(self):
        employee1 = {
            "first_name": "Anna",
            "last_name": "Andersson",
            "email": "anna.andersson1@example.com"
        }
        employee2 = {
            "first_name": "Anna",
            "last_name": "Andersson",
            "email": "anna.andersson2@example.com"
        }
        
        response1 = self.client.post('/api/employees/', employee1, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        
        response2 = self.client.post('/api/employees/', employee2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        self.assertEqual(response.data[0]['first_name'], 'Anna')
        self.assertEqual(response.data[0]['last_name'], 'Andersson')
        self.assertEqual(response.data[1]['first_name'], 'Anna')
        self.assertEqual(response.data[1]['last_name'], 'Andersson')
        self.assertNotEqual(response.data[0]['email'], response.data[1]['email'])

    def test_can_readd_employee_after_deletion(self):
        employee_data = {
            "first_name": "Anna",
            "last_name": "Andersson",
            "email": "anna@example.com"
        }
        
        response = self.client.post('/api/employees/', employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        employee_id = response.data['id']
        
        response = self.client.get('/api/employees/')
        self.assertEqual(len(response.data), 1)
        
        response = self.client.delete(f'/api/employees/{employee_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.get('/api/employees/')
        self.assertEqual(len(response.data), 0)
        
        response = self.client.post('/api/employees/', employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get('/api/employees/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], 'anna@example.com')

    def test_cannot_add_employee_with_invalid_email(self):
        invalid_emails = ['notanemail', 'test@', '@example.com', 'test@.com', 'test..test@example.com']
        
        for invalid_email in invalid_emails:
            employee_data = {
                "first_name": "Anna",
                "last_name": "Andersson",
                "email": invalid_email
            }
            
            response = self.client.post('/api/employees/', employee_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('email', response.data)

    def test_delete_nonexistent_employee_returns_404(self):
        response = self.client.delete('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    def test_cannot_add_employee_with_missing_fields(self):
        missing_first_name = {
            "last_name": "Andersson",
            "email": "anna@example.com"
        }
        response = self.client.post('/api/employees/', missing_first_name, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', response.data)
        
        missing_last_name = {
            "first_name": "Anna",
            "email": "anna@example.com"
        }
        response = self.client.post('/api/employees/', missing_last_name, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('last_name', response.data)
        
        missing_email = {
            "first_name": "Anna",
            "last_name": "Andersson"
        }
        response = self.client.post('/api/employees/', missing_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_cannot_add_employee_with_too_long_fields(self):
        too_long_first_name = {
            "first_name": "A" * 101,
            "last_name": "Andersson",
            "email": "anna@example.com"
        }
        response = self.client.post('/api/employees/', too_long_first_name, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', response.data)
        
        too_long_last_name = {
            "first_name": "Anna",
            "last_name": "B" * 101,
            "email": "anna@example.com"
        }
        response = self.client.post('/api/employees/', too_long_last_name, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('last_name', response.data)

