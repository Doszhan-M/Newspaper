# Generated by Django 3.1.5 on 2021-03-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20210308_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_en',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_ru',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
