from django.contrib.auth.models import User
from django.utils.text import slugify
from django.test import TestCase
from wiki.models import Page


class WikiTests(TestCase):
    def test_signup(self):
        test_user = User.objects.create_user(
            username='test', 
            password='test'
            )

        self.client.login(
            username='test', 
            password='test'
        )
        print(self.request.user.username)
