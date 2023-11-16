from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import index, view_fav, add_fav, add_complaint, view_complaint, search, sign_up

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('Management:Home')
        self.assertEqual(resolve(url).func, index)

    def test_view_fav_url_resolves(self):
        url = reverse('Management:View_Favourite')
        self.assertEqual(resolve(url).func, view_fav)

    def test_add_fav_url_resolves(self):
        url = reverse('Management:Add_Favourite')
        self.assertEqual(resolve(url).func, add_fav)

    def test_add_complaint_url_resolves(self):
        url = reverse('Management:Add_Complaint')
        self.assertEqual(resolve(url).func, add_complaint)

    def test_view_complaint_url_resolves(self):
        url = reverse('Management:View_Complaint')
        self.assertEqual(resolve(url).func, view_complaint)

    def test_search_url_resolves(self):
        url = reverse('Management:Search')
        self.assertEqual(resolve(url).func, search)

    def test_sign_up_url_resolves(self):
        url = reverse('Management:Sign_Up')
        self.assertEqual(resolve(url).func, sign_up)
