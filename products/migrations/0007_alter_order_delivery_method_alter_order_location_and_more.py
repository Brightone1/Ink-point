# Generated by Django 4.1.5 on 2023-01-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_imageupload_owner_alter_imageupload_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('dispatch-store', 'Dispatch store'), ('door-delivery', 'Door delivery')], default='door-delivery', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('cash', 'Cash'), ('mpesa', 'M-pesa'), ('bank', 'Bank')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'Cart'), ('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=30),
        ),
    ]
