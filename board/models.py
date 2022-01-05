from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    #modify_date = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    @property
    def unread_notification(self):
        i = 0

        for notification in self.user.user_notification.all():
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

'''
Post <- 누군가 댓글을 달면 알림
Post 작성자 Post's Comment 작성자에게
'''
class Notification(BaseModel):
    user = models.ForeignKey(User, related_name='user_notification', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    invoke = models.ForeignKey(User, related_name='invoke_notification', on_delete=models.CASCADE)
    read_date = models.DateTimeField(null=True, blank=True)

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET("Deleted:User"), related_name='author_comment')
    content = models.TextField()
    create_date = models.DateTimeField()
    #modify_date = models.DateTimeField(null=True, blank=True)
    #replied_to = models.ForeignKey('self', on_delete=models.SET("Deleted:Comment"), null=True)
    #liked = models.ManyToManyField(User, related_name='liked_comment')
    #disliked = models.ManyToManyField(User, related_name='disliked_comment')
    
    def __str__(self):
        return self.content
