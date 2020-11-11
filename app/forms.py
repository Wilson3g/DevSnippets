from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'title_tag': forms.TextInput(attrs={'class': 'input-field'}),
            'body': forms.Textarea(attrs={'class': 'input-field'})
        }