# Generated by Django 4.2.7 on 2023-12-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_alter_brandmodel_slug'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminpost',
            name='brand_name',
        ),
        migrations.AddField(
            model_name='adminpost',
            name='brand',
            field=models.ManyToManyField(blank=True, null=True, to='brands.brandmodel'),
        ),
    ]
