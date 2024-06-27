from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_content(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'خانه')
        
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template_use(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')