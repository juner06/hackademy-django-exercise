# Generated by Django 4.1.6 on 2023-02-15 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity1', '0004_user_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
