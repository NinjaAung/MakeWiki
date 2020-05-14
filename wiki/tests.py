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
        print(test_user.id)
        self.assertEqual(test_user.username,'test')
        

def test_create_page(self):
    test_user = User.objects.create()
    # Post data to be sent via the form
    post_data = {
        'title': 'asdasdasdasd',
        'content': 'asdasdasdasdasdasd',
        'author': test_user.id
    }

    res = self.client.post('/create/', data=post_data)

    self.assertEqual(res.status_code, 302)

    page_object = Page.objects.get(title='asdasdasdasd')

    self.assertEqual(page_object.title, 'asdasdasdasdasdasd')

