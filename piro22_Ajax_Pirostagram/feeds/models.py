from django.db import models

class Feed(models.Model):
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    like_count = models.PositiveIntegerField(default=0)