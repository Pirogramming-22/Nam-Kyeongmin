from django.db import models
from tools.models import Tool

class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=20)
    image = models.ImageField('Image', upload_to='images/%Y%m%d', blank=True)
    explain = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도')
    develop_tool = models.ForeignKey(Tool, verbose_name='예상 개발툴', on_delete=models.CASCADE)
    created_at = models.DateTimeField('최초 등록시간', auto_now_add=True)
    updated_at = models.DateTimeField('최종 수정시간', auto_now=True)
    is_like = models.BooleanField(default=False)