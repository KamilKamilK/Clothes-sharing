# Generated by Django 3.1.1 on 2020-10-07 13:10

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200914_1720'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]