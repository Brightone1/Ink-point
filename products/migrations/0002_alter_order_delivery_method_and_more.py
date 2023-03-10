# Generated by Django 4.1.5 on 2023-01-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('dispatch-store', 'Dispatch store'), ('door-delivery', 'Door delivery')], default='door-delivery', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('mpesa', 'M-pesa'), ('cash', 'Cash'), ('bank', 'Bank')], default='cash', max_length=50),
        ),
    ]
