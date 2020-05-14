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
    page_object = Page.objects.get(title='asdasdasdasd')

    self.assertEqual(res.status_code, 302)
    self.assertEqual(page_object.title, 'asdasdasdasd')
    self.assertEqual(page_object.content, 'asdasdasdasdasdasd')

def test_edit_page(self):
        test_user = User.objects.create()


        page = Page.objects.create(
            title='asdasdasdasd', 
            content='asdasdasdasdasdasd', 
            author=test_user.id
            )

        page.save() 

        post_data = {
            'title': 'zxczxczxczxczxczxczxc',
            'content': 'zxczxczxczxczxczxczxczxc',
            'author': test_user.id
        }

        res = self.client.post('/{}/'.format(slugify(page.title)), post_data)
        self.assertEqual(res.status_code, 302)

def test_edit_page_no_author(self):
    test_user = User.objects.create()


    page = Page.objects.create(
        title='asdasdasdasd', 
        content='asdasdasdasdasdasd', 
        author='ssdfsdfsdfsd',
    )

    page.save() 

    post_data = {
        'title': 'zxczxczxczxczxczxczxc',
        'content': 'zxczxczxczxczxczxczxczxc',
        'author': test_user.id
    }

    res = self.client.post('/{}/'.format(slugify(page.title)), post_data)
    self.assertEqual(res.status_code != 302)

    

