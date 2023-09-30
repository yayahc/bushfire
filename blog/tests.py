from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='TestUser',
            email=' test@mail.co',
            password='secret'

        )

        self.post = Post.objects.create(
            title='A good title',
            body='nice body content',
            author=self.user
        )
        post = self.post

        self.post_id = post.pk

    def test_string_representation(self):
        post = Post(title='a simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{ self.post.body }', 'nice body content')
        self.assertEqual(f'{self.post.author}', 'TestUser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):

        response = self.client.get('/post/{}/' .format(self.post_id))
        #response = self.client.get('/post/1/')
        no_response = self.client.get('post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'testing',
            'body': 'gibberish',
            'author': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testing')

    def test_post_edit_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'testing edited ',
            'body': ' gibberish testing'
        })

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
