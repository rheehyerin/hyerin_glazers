from django import forms
from blog.models import  Portfolio_content
from blog.models import Post

class VideoForm(forms.ModelForm):
    class Meta:
        model = Portfolio_content
        fields = ('title', 'video', 'content',)
