from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET("Deleted:User"))
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET("Deleted:User"))
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    replied_to = models.ForeignKey('self', on_delete=models.SET("Deleted:Comment"), null=True)

    def __str__(self):
        return self.content
