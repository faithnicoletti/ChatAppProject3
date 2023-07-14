from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

class Chat(models.Model):
    content = models.TextField(max_length=600)
    timestamp = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User)

def __str__(self):
    return f"Chat {self.id}"
