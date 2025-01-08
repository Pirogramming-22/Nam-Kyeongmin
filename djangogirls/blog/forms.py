from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # 폼을 만들때 사용할 모델
        fields = ("title", "text",) # 폼에서 보일 속성들