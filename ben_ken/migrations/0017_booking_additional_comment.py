# Generated by Django 3.2.16 on 2023-02-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ben_ken', '0016_booking_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='additional_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]