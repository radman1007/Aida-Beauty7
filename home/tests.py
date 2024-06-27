from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)