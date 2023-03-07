# Generated by Django 4.1.5 on 2023-02-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_cart_consent_alter_order_delivery_method_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('entry', models.TextField(null=True)),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
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
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('cart', 'Cart'), ('pending', 'Pending')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('out_of_stock', 'Out of Stock')], default='available', max_length=50),
        ),
    ]
