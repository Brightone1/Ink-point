from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """The Subject someone is writing about"""
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the Model"""
        return self.title


class Entry(models.Model):
    """The exact content of the subject"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """String representation of the Model"""
        return f"{self.text[:50]}..."

