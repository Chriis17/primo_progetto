# Generated by Django 5.1.3 on 2025-02-05 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articolo_options_alter_giornalista_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='dataPubblicazione',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 2, 5, 11, 54, 25, 438416)),
        ),
        migrations.AlterField(
            model_name='giornalista',
            name='dataNascita',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 2, 5, 11, 54, 25, 438416)),
        ),
    ]
