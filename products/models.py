from django.db import models
from django.contrib.auth.models import User


class ImageUpload(models.Model):
    owner = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', default='Instagram.png', blank=True, null=True)


class Category(models.Model):
    """Category of the products"""
    title = models.CharField(max_length=200, blank=False, null=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """String rep of the model"""
        return self.title


class SubCategory(models.Model):
    """sub-category of the products"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        """String rep of the model"""
        return self.title


class Product(models.Model):
    """Product itself"""

    AVAILABLE = 'available'
    OUT_OF_STOCK = 'out of stock'

    availability = {
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock')
    }
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/', blank=False, null=True)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=availability, default=AVAILABLE)
    price = models.DecimalField(decimal_places=2, blank=False, max_digits=1000000, null=True)

    def __str__(self):
        """String rep of the model"""
        return self.name


class Order(models.Model):
    """Product order"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField(blank=False, null=True)
    location = models.CharField(max_length=200, blank=False, null=True)

    CASH = 'cash'
    MPESA = 'mpesa'
    BANK = 'bank'

    payment_method = {
        ('cash', 'Cash'),
        ('mpesa', 'M-pesa'),
        ('bank', 'Bank')
    }
    means_of_payment = models.CharField(max_length=50, choices=payment_method, default=CASH, blank=False, null=True)

    DISPATCH_STORE = 'dispatch-store'
    DOOR_DELIVERY = 'door-delivery'

    dispatch = {
        ('dispatch-store', 'Dispatch store'),
        ('door-delivery', 'Door delivery'),
    }
    delivery_method = models.CharField(max_length=50, choices=dispatch, default=DOOR_DELIVERY, blank=False, null=True)

    PENDING = 'pending'
    COMPLETED = 'completed'
    CART = 'cart'

    Order_status = {
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cart', 'Cart')
    }
    status = models.CharField(max_length=30, choices=Order_status, default=PENDING)
    quantity = models.PositiveIntegerField(blank=False, null=True)
    date_placed = models.DateField(auto_now_add=True)

    def __str__(self):
        """String rep of the model"""
        return self.product.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    YES = 'yes'
    NO = 'no'

    agreement = {
        ('yes', 'Yes'),
        ('no', 'No')
    }
    consent = models.CharField(max_length=50, choices=agreement, default=YES)

    def __str__(self):
        """String rep of the model"""
        return self.product.name

