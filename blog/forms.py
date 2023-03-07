from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['username', 'text']
		labels = {'username': 'Username',
		         'text': 'Comment'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80,
			      'placeholder': 'Add comment'})}