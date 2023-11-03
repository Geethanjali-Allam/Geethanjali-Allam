from .models import Employee
from django.test import TestCase
from django.urls import reverse

class ManagementViewsTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('Management:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/index.html')

    def test_view_fav_view(self):
        response = self.client.get(reverse('Management:view_fav'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/favourite.html')

    def test_add_fav_view(self):
        response = self.client.get(reverse('Management:add_fav'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/add_favourite.html')

        # Test POST request
        data = {'new_favorite': 'New Favorite'}
        response = self.client.post(reverse('Management:add_fav'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(len(favorites), 1)  # Check if the favorite was added

    def test_add_complaint_view(self):
        response = self.client.get(reverse('Management:add_complaint'))
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
        response = self.client.post(reverse('Management:add_complaint'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(len(complaint_author), 1)  # Check if the complaint was added

    def test_view_complaint_view(self):
        response = self.client.get(reverse('Management:view_complaint'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/complaint.html')

    def test_search_view(self):
        response = self.client.get(reverse('Management:search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Management/search.html')

        # Test POST request
        data = {'query': 'John Doe'}  # Assuming 'John Doe' exists in Employee objects
        response = self.client.post(reverse('Management:search'), data)
        self.assertEqual(response.status_code, 200)  # Check if the search result is displayed

    def test_sign_up_view(self):
        response = self.client.get(reverse('Management:sign_up'))
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
        response = self.client.post(reverse('Management:sign_up'), data)
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Employee.objects.count(), 1)  # Check if a new employee was added to the database
