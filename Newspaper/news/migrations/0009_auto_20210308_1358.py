# Generated by Django 3.1.5 on 2021-03-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20210308_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='headline_en',
            field=models.CharField(help_text='Заголовок', max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='headline_ru',
            field=models.CharField(help_text='Заголовок', max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text_ru',
            field=models.TextField(null=True),
        ),
    ]
