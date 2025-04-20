from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()  # 1, 2, 3, or 4

    def __str__(self):
        return self.text

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)