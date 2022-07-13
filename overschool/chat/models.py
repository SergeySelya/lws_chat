from django.db import models
from django.contrib.auth.models import User


class Groups(models.Model):
    group_name = models.TextField()

    def __str__(self):
        return self.group_name


class Members(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)


class Message(models.Model):
    username = models.CharField(max_length=50)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

# class Message(models.Model):
#     user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
#     group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
#     message = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('date_added',)
