# Generated by Django 5.0.3 on 2024-03-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='popular',
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=20),
        ),
    ]
