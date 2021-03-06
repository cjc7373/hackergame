# Generated by Django 3.1.1 on 2020-09-29 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0005_auto_20200829_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreboard',
            name='score',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
