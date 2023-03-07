from django.db import models
from products.models import Product


class Review(models.Model):
    """Peoples reviews and comments"""
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200, blank=False, null=True)
    entry = models.TextField(blank=False, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String rep of the model"""
        return self.username
