# Generated by Django 3.2.16 on 2023-02-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ben_ken', '0018_auto_20230207_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='provided_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
