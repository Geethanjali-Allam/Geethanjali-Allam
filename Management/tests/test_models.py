import pytest
from django.test import TestCase
from ..models import Employee

class TestEmployeeModel(TestCase):
    def setUp(self):
        # Set up any necessary data before each test
        self.employee_data = {
            "Name": "John Doe",
            "Email": "john@example.com",
            "Password": "securepassword",
            "Position": "Developer",
            "Salary": 50000,
        }

    def test_employee_creation(self):
        # Test creating an Employee instance
        employee = Employee.objects.create(**self.employee_data)

        # Check if the created instance has the expected attributes
        assert employee.Name == "John Doe"
        assert employee.Email == "john@example.com"
        assert employee.Password == "securepassword"
        assert employee.Position == "Developer"
        assert employee.Salary == 50000

    def test_employee_str_representation(self):
        # Test the __str__ method of the Employee model
        employee = Employee.objects.create(**self.employee_data)

        # Check if the string representation is as expected
        expected_str = f"{employee.id}: {employee.Name} is {employee.Position} with salary of {employee.Salary}. Email:{employee.Email} and Password:{employee.Password}"
        assert str(employee) == expected_str


