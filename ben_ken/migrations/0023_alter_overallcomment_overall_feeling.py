# Generated by Django 3.2.16 on 2023-02-15 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ben_ken', '0022_alter_overallcomment_booking_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overallcomment',
            name='overall_feeling',
            field=models.CharField(choices=[('happy', 'happy'), ('indifferent', 'indifferent'), ('unhappy', 'unhappy')], max_length=11),
        ),
    ]
