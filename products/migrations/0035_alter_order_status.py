# Generated by Django 4.1.6 on 2023-02-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_alter_order_delivery_method_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending'), ('cart', 'Cart')], default='pending', max_length=30),
        ),
    ]
