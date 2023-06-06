# Generated by Django 4.2.1 on 2023-06-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_review_review_date'),
        ('accounts', '0005_remove_userprofile_favorite_films'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite_films',
            field=models.ManyToManyField(blank=True, to='films.film'),
        ),
    ]
