# Generated by Django 4.1.6 on 2023-02-20 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_order_delivery_method_alter_order_status'),
        ('reviews', '0005_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
