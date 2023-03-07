# Generated by Django 4.1.5 on 2023-01-28 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(null=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('out_of_stock', 'Out of Stock')], default='available', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000000, null=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('means_of_payment', models.CharField(choices=[('bank', 'Bank'), ('cash', 'Cash'), ('mpesa', 'M-pesa')], default='cash', max_length=50)),
                ('delivery_method', models.CharField(choices=[('door-delivery', 'Door delivery'), ('dispatch-store', 'Dispatch store')], default='door-delivery', max_length=50)),
                ('status', models.CharField(choices=[('cart', 'Cart'), ('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=30)),
                ('quantity', models.PositiveIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]