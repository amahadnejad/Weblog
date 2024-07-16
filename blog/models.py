from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
