# Generated by Django 2.1.5 on 2019-02-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythontutorial', '0002_videouploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='videouploader',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
