from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *
from app.urls import *

class TestUrls(SimpleTestCase):

    def test_home_urls_is_resolved(self):   
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_searchBook_urls_is_resolved(self):
        url = reverse('searchBook')
        self.assertEquals(resolve(url).func, searchBook)

    def test_aboutUs_urls_is_resolved(self):   
        url = reverse('aboutUs')
        self.assertEquals(resolve(url).func, aboutUs)
    
    def test_contactUs_urls_is_resolved(self):   
        url = reverse('contactUs')
        self.assertEquals(resolve(url).func, contactUs)
    
    def test_register_urls_is_resolved(self):   
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
        
    def test_profile_urls_is_resolved(self):   
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)