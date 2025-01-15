from django.db import models

class Tool(models.Model):
    name = models.CharField('이름', max_length=20)
    type = models.CharField('종류', max_length=20)
    explain = models.TextField('개발툴 설명')