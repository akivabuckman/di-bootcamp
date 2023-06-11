# Generated by Django 4.2.1 on 2023-06-08 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_count', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('room_id', models.ForeignKey(limit_choices_to=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], on_delete=django.db.models.deletion.DO_NOTHING, related_name='booking_roomid', to='visitors_app.room')),
                ('visitor_id', models.ManyToManyField(related_name='visitor_booking', to='visitors_app.visitoruserprofile')),
            ],
        ),
    ]
