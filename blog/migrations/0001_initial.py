# Generated by Django 4.1.6 on 2023-02-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('intro', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]