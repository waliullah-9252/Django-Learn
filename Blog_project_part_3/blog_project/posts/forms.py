from django import forms
from .models import Post, Commnet

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commnet
        fields = ['name', 'email', 'body']