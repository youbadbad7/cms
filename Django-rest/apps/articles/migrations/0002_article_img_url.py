# Generated by Django 3.1 on 2020-08-27 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img_url',
            field=models.CharField(max_length=200, null=True, verbose_name='图片地址'),
        ),
    ]
