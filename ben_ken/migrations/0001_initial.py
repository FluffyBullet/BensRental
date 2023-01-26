# Generated by Django 3.2.16 on 2023-01-19 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_reference', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=25)),
                ('contact_number', models.IntegerField()),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(max_length=200)),
                ('address_line_3', models.CharField(max_length=200)),
                ('address_line_4', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=9)),
                ('email_address', models.EmailField(max_length=254)),
                ('preference_of_contact', models.CharField(max_length=30)),
                ('admin_comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_reference', models.SmallAutoField(primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('number_of_o18', models.PositiveSmallIntegerField()),
                ('number_of_u18', models.PositiveSmallIntegerField()),
                ('number_of_pets', models.PositiveSmallIntegerField()),
                ('total_guest', models.PositiveSmallIntegerField()),
                ('account_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ben_ken.account')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('messages_thread', models.IntegerField(primary_key=True, serialize=False)),
                ('message_header', models.CharField(max_length=50)),
                ('message_text', models.TextField()),
                ('report', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taks_reference', models.IntegerField(primary_key=True, serialize=False)),
                ('task_description', models.CharField(max_length=200)),
                ('task_complete', models.BooleanField(default=False)),
                ('booking_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ben_ken.booking')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ben_ken.account')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_reference', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('overall_comment', models.CharField(max_length=200)),
                ('personal_comment', models.CharField(max_length=200)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ben_ken.booking')),
                ('user_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ben_ken.account')),
            ],
        ),
    ]