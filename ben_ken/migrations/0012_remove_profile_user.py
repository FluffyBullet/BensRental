# Generated by Django 3.2.16 on 2023-02-01 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ben_ken', '0011_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]