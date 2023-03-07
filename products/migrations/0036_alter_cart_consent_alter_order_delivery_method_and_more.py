# Generated by Django 4.1.6 on 2023-02-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='consent',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('dispatch-store', 'Dispatch store'), ('door-delivery', 'Door delivery')], default='door-delivery', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('mpesa', 'M-pesa'), ('cash', 'Cash'), ('bank', 'Bank')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'Cart'), ('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('available', 'Available')], default='available', max_length=50),
        ),
    ]
