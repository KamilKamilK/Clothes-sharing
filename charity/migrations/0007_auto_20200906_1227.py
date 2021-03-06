# Generated by Django 3.1.1 on 2020-09-06 12:27

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_auto_20200906_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
