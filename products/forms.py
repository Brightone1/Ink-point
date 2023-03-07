from django import forms
from .models import Order, Cart


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'location', 'means_of_payment', 'delivery_method', 'quantity']
        labels = {'phone_number': 'Phone number', 'location': 'Location',
                  'means_of_payment': 'Payment Method', 'delivery_method': 'Delivery method',
                  'quantity': 'Quantity'}


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['consent']
        labels = {'consent': ''}
