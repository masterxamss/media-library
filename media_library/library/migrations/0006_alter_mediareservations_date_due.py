# Generated by Django 5.1.1 on 2024-09-23 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_mediareservations_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediareservations',
            name='date_due',
            field=models.DateField(default=datetime.timedelta(days=7)),
        ),
    ]
