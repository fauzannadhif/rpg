# Generated by Django 4.2.11 on 2024-04-30 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('daily_bookings', models.TextField()),
            ],
        ),
    ]
