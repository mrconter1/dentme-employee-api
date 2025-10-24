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

