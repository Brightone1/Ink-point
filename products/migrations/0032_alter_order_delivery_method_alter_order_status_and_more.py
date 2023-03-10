# Generated by Django 4.1.6 on 2023-02-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_alter_cart_consent_alter_order_delivery_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('dispatch-store', 'Dispatch store'), ('door-delivery', 'Door delivery')], default='door-delivery', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cart', 'Cart'), ('completed', 'Completed')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('available', 'Available')], default='available', max_length=50),
        ),
    ]
