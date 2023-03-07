# Generated by Django 4.1.6 on 2023-02-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_cart_consent_alter_order_delivery_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='consent',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank'), ('mpesa', 'M-pesa')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cart', 'Cart'), ('completed', 'Completed')], default='pending', max_length=30),
        ),
    ]