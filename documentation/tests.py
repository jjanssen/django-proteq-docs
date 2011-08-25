from django.test import TestCase
from django.test.client import Client
from documentation.views import documentation
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User


class DocumentationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = settings.LOGIN_URL
        User.objects.create_user('testuser', 'test@example.com', 'testpw')
        v = User.objects.create_user('teststaff', 'test@example.com', 'testpw')
        v.is_staff = True
        v.save()

    def test_no_anonymous(self):
        c = self.client
        response = c.get(reverse(documentation, args=['index.html']))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.login_url, response['location'])

    def test_no_regular(self):
        c = self.client
        c.login(username='testuser', password='testpw')
        response = c.get(reverse(documentation, args=['index.html']))
        self.assertIn(self.login_url, response['location'])

    def test_staff(self):
        c = self.client
        c.login(username='teststaff', password='testpw')
        response = c.get(reverse(documentation, args=['index.html']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'admin/login.html')
        self.assertNotEqual(None, response.content)
