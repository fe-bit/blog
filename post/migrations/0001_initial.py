# Generated by Django 3.2.7 on 2022-08-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('template_name', models.CharField(max_length=500)),
            ],
        ),
    ]
