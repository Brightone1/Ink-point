# Generated by Django 4.1.6 on 2023-02-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_order_means_of_payment_alter_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('dispatch-store', 'Dispatch store'), ('door-delivery', 'Door delivery')], default='door-delivery', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank'), ('mpesa', 'M-pesa')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cart', 'Cart')], default='pending', max_length=30),
        ),
    ]
