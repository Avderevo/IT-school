from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=250)
    paid = models.BooleanField(default=False)
    total_homework = models.PositiveIntegerField()
    homework_done = models.IntegerField()
    test_score = models.CharField(max_length=50)



class Chat(models.Model):
    chat_topic = models.CharField(max_length=150)


class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data_message = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

