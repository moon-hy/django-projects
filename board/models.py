from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET('Deleted:User'), related_name='author_post')
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='liked_post')
    disliked = models.ManyToManyField(User, related_name='disliked_post')
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    @property
    def update_hits(self):
        self.hits += 1
        self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET("Deleted:User"), related_name='author_comment')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    replied_to = models.ForeignKey('self', on_delete=models.SET("Deleted:Comment"), null=True)
    liked = models.ManyToManyField(User, related_name='liked_comment')
    disliked = models.ManyToManyField(User, related_name='disliked_comment')
    
    def __str__(self):
        return self.content
