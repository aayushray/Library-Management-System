from django.test import TestCase, Client
from django.urls import reverse
from app.urls import *
from app.models import *
import json

class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.searchBook_url = reverse('searchBook')
        self.aboutUs_url = reverse('aboutUs')
        self.issueBook_url = reverse('issueBook')
        self.contactUs_url = reverse('contactUs')
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')

        self.book = Book.objects.create(
            book_name='Antenna Theory and Design',
            book_author='Balanis',
            book_publisher='McGraw Hill',
            book_price=1999,
            is_issued=False,
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_aboutUs_GET(self):
        response = self.client.get(self.aboutUs_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'aboutUs.html')
    
    def test_contactUs_GET(self):
        response = self.client.get(self.contactUs_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'contactUs.html')
    
    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'profile.html')