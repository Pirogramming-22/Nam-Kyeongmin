from django.db import models

class Review(models.Model):
    poster = models.FileField(upload_to='templates/poster/', blank=True)
    title = models.TextField()
    release = models.TextField()
    genre = models.CharField(max_length=200)
    stars = models.FloatField()
    director = models.TextField()
    actor = models.TextField()
    running_time = models.TextField()
    summary = models.TextField()