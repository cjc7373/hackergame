# Generated by Django 3.1 on 2020-09-08 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0004_auto_20200908_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.ManyToManyField(related_name='admin_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
