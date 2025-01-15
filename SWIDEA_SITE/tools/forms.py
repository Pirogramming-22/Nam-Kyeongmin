from django import forms
from .models import Tool

class ToolFrom(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('__all__')