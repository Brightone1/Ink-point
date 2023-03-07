from django import forms
from .models import Blog, Entry


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title']
        labels = {'title': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Note'}
        widgets = {'text': forms.Textarea(attrs={
            'cols': 100,
            'placeholder': 'Add notes here'
        })}

