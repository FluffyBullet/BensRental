# Generated by Django 3.2.16 on 2023-01-31 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ben_ken', '0008_auto_20230131_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ben_ken.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ben_ken.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='admin_commnets',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='preference_of_contact',
            field=models.CharField(choices=[('phone', 'Phone'), ('post', 'Post'), ('post', 'letter')], default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_reference',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
