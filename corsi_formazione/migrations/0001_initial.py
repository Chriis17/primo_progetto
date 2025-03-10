# Generated by Django 5.1.3 on 2025-02-12 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=20)),
                ('descrizione', models.TextField()),
                ('data_inizio', models.DateField(blank=True, default=datetime.datetime(2025, 2, 12, 9, 40, 10, 545025))),
                ('data_fine', models.DateField(blank=True, default=datetime.datetime(2025, 2, 12, 9, 40, 10, 545025))),
                ('posti_disponibili', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Corso',
                'verbose_name_plural': 'Corsi',
            },
        ),
    ]
