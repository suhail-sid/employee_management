from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Employee

class EmployeeTests(APITestCase):
    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {'name': 'Suhail Siddiqui', 'email': 'suhailsiddiqui1530@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        url = reverse('employee-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_employee(self):
        employee = Employee.objects.create(name='Suhail Siddiqui', email='suhailsiddiqui1530@gmail.com')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        employee = Employee.objects.create(name='Suhail Siddiqui', email='suhailsiddiqui1530@gmail.com')
        url = reverse('employee-detail', args=[employee.id])
        data = {'name': 'Siddiqui Suhail'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_delete_employee(self):
        employee = Employee.objects.create(name='Suhail', email='suhailsiddiqui1530@gmail.com')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
