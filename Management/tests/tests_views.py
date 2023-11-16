from ..models import Employee
from django.test import TestCase
from django.urls import reverse

class ManagementViewsTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('Management:Home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/index.html')

    def test_view_fav_view(self):
        response = self.client.get(reverse('Management:View_Favourite'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/favourite.html')

    def test_add_fav_view(self):
        response = self.client.get(reverse('Management:Add_Favourite'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/add_favourite.html')

        # Test POST request
        data = {'new_favorite': 'New Favorite'}
        response = self.client.post(reverse('Management:Add_Favourite'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect

    def test_add_complaint_view(self):
        response = self.client.get(reverse('Management:Add_Complaint'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/add_complaint.html')

        # Test POST request
        data = {
            'name': 'John Doe',
            'sender': 'johndoe@example.com',
            'c_type': 'General',
            'subject': 'Test Complaint',
            'message': 'This is a test complaint.'
        }
        response = self.client.post(reverse('Management:Add_Complaint'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect

    def test_view_complaint_view(self):
        response = self.client.get(reverse('Management:View_Complaint'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/complaint.html')

    def test_search_view(self):
        response = self.client.get(reverse('Management:Search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/search.html')

        # Test POST request
        data = {'query': 'John Doe'}  # Assuming 'John Doe' exists in Employee objects
        response = self.client.post(reverse('Management:Search'), data)
        self.assertEqual(response.status_code, 200)  # Check if the search result is displayed

    def test_sign_up_view(self):
        response = self.client.get(reverse('Management:Sign_Up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/signup.html')

        # Test POST request
        data = {
            'Name': 'New Employee',
            'Email': 'newemployee@example.com',
            'Password': 'password123',
            'Position': 'Developer',
            'Salary': 50000
        }
        response = self.client.post(reverse('Management:Sign_Up'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Employee.objects.count(), 1)  # Check if a new employee was added to the database
