# Generated by Django 4.2.7 on 2023-12-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
