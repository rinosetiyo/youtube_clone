from django import forms
from youtubeClone.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment",]