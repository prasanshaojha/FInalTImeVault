# Generated by Django 5.0.8 on 2024-12-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0005_bloginteraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicletter',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
