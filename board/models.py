from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta, datetime, timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def unread_notification(self):
        i = 0
        for notification in self.user.notification.all():
            if notification.read_date is None:
                i += 1
        return i

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=10)
    class Meta:
            verbose_name_plural = "Categories"
    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET('Deleted:User'), related_name='author_post')
    subject = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='liked_post')
    disliked = models.ManyToManyField(User, related_name='disliked_post')
    hits = models.PositiveIntegerField(default=0)

    @property
    def is_recent(self):
        return (datetime.now(timezone.utc) - self.create_date) < timedelta(days=1)

    @property
    def update_hits(self):
        self.hits += 1
        self.save()
        
    def __str__(self):
        return self.subject


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET("Deleted:User"), related_name='author_comment')
    content = models.TextField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content


'''
Post <- 누군가 댓글을 달면 알림
Post 작성자 Post's Comment 작성자에게
'''
class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notification', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    read_date = models.DateTimeField(null=True, blank=True)

    @property
    def invoked_user(self):
        return self.comment.author
