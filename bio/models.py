from email.policy import default
from django.db import models

# Create your models here.

class MyBio(models.Model):
    slackUsername = models.CharField(max_length=30)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.slackUsername