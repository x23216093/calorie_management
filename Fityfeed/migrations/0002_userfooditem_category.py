# Generated by Django 3.2.16 on 2024-03-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fityfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfooditem',
            name='category',
            field=models.ManyToManyField(to='Fityfeed.Category'),
        ),
    ]
