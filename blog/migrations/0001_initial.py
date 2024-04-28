# Generated by Django 5.0.3 on 2024-03-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]