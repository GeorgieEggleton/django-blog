from .models import Comment 
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)  # trailing commer important or python reads as string not tuple
