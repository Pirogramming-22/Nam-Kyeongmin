from django.db import models

class Review(models.Model):
    title = models.TextField()
    release = models.TextField()
    genre = models.CharField(max_length=200)
    stars = models.FloatField()
    director = models.TextField()
    actor = models.TextField()
    running_time = models.TextField()
    summary = models.TextField()