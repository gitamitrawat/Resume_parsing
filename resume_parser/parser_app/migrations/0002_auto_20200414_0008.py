# Generated by Django 2.2.10 on 2020-04-13 18:38

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user_id',
            field=models.IntegerField(null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
