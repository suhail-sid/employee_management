from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee 

class EmployeeTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.employee_data = {
            'name': 'Suhail',
            'position': 'Developer',
            'salary': 50000
        }

    def test_create_employee(self):
        response = self.client.post(reverse('employee-list'), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_employee_and_update_name(self):
        # First create an employee
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.get(reverse('employee-detail', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update employee's name
        response = self.client.patch(reverse('employee-detail', args=[employee.id]), {'name': 'Updated Name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Name')

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.delete(reverse('employee-detail', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
