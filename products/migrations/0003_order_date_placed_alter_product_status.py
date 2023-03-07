# Generated by Django 4.1.5 on 2023-01-28 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_order_delivery_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_placed',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('available', 'Available')], default='available', max_length=50),
        ),
    ]
