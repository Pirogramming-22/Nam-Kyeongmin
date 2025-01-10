from django.db import models

class Review(models.Model):
    poster = models.FileField(upload_to='templates/poster/', blank=True)
    title = models.TextField()
    release = models.TextField()
    GENRE_CHOICES = [
        ('act', '액션'),
        ('dra', '드라마'),
        ('roco', '로맨스/코미디'),
        ('sf', 'SF'),
        ('hor', '스릴러'),
        ('ani', '애니메이션'),
        ('fan', '판타지'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='dra')
    stars = models.FloatField()
    director = models.TextField()
    actor = models.TextField()
    running_time = models.TextField()
    summary = models.TextField()