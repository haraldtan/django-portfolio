from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.
class TestUrls:
    def test_blog_url(self):
        path = reverse('blog')
        assert resolve(path).view_name == 'blog'