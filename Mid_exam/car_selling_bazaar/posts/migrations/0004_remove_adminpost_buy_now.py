# Generated by Django 4.2.7 on 2023-12-20 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminpost',
            name='buy_now',
        ),
    ]
