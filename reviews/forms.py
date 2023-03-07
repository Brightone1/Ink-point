from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'entry']
        labels = {'username': 'Username', 'entry': 'Entry'}
        widgets = {'entry': forms.Textarea(attrs={'cols': 80})}
