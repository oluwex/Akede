from django import forms
from .models import Article

class CreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'name',
            'content',
            'image',
            'category',
            'draft',
            'publish_date',
        ]