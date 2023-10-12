from django import forms
from .models import Tweet, FacebookPost

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'user']

class FacebookPostForm(forms.ModelForm):
    class Meta:
        model = FacebookPost
        fields = ['message', 'user_id']

