from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


class PostListViewTest(TestCase):
    def setUp(self):
        self.author = get_user_model().objects.create_user(username='test_user', password='12345')
        self.post = Post.objects.create(author=self.author, title='test_title', description='test_description',
                                        status='pub')

    def test_posts_list_view_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_posts_list_view_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_posts_list_page_contains_title(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, 'test_title')

    def test_posts_list_page_contains_description(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, 'test_description')

