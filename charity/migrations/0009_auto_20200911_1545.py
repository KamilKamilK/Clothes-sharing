# Generated by Django 3.1.1 on 2020-09-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0008_auto_20200907_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.CharField(choices=[('fu', 'Fundacja'), ('or', 'Organizacja pozarządowa'), ('ct', 'Zbiórka lokalna')], max_length=2),
        ),
    ]
