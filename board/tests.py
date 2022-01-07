from contextlib import nullcontext
from datetime import timezone
from django.contrib.auth import get_user_model
from django.test import TestCase

from board.models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username='test', password='123')
        Post.objects.create(
            author=user, 
            subject='test_sbject', 
            content='test_content',
            create_date=timezone.now(),
            modify_date=None,
            liked=None,
            disliked=None,
            hits=0)

    def test_post_subject(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.subject, 'test_subject')

    def test_post_content(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.content, 'test_content')

    


