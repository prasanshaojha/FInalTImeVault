# Generated by Django 5.0.8 on 2024-11-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicletter',
            name='feature_photo',
            field=models.ImageField(blank=True, null=True, upload_to='public_letters/photos/'),
        ),
    ]
