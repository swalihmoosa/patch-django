# Generated by Django 3.2.9 on 2021-11-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_testimonial_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
