from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post, Comment


# class PostListViewTest(TestCase):
#     def setUp(self):
#         self.author = get_user_model().objects.create_user(username='test_user', password='12345')
#         self.post = Post.objects.create(author=self.author, title='test_title', description='test_description',
#                                         status='pub')
#
#     def test_posts_list_view_by_url(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_posts_list_view_by_name(self):
#         response = self.client.get(reverse('post_list'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_posts_list_page_contains_title(self):
#         response = self.client.get(reverse('post_list'))
#         self.assertContains(response, 'test_title')
#
#     def test_posts_list_page_contains_description(self):
#         response = self.client.get(reverse('post_list'))
#         self.assertContains(response, 'test_description')


class PostDetailViewTest(TestCase):
    def setUp(self):
        # Create Test Author & Post
        self.author = get_user_model().objects.create_user(username='test_user', password='12345')
        self.post = Post.objects.create(author=self.author, title='Test title', description='Test Description',
                                        status='pub')

        # Create Test Comment
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.author,
            text="This is a test comment",
            helpful=True,
            is_active=True
        )

    def test_post_detail_view_status_code(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_template_used(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_detail_page_contains_title(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, 'Test title')

    def test_post_detail_page_contains_description(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, 'Test Description')

    def test_post_detail_page_contains_comment_text(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, 'This is a test comment')

