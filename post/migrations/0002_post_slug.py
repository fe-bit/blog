# Generated by Django 3.2.7 on 2022-08-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
    ]