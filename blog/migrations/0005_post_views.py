# Generated by Django 5.0.3 on 2024-03-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_popular_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
