from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Post


class PostViewTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user("author", password="x")
        self.post = Post.objects.create(
            author=user, title="Hello", text="Body", published_date=timezone.now()
        )

    def test_list_shows_published_post(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, "Hello")

    def test_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
