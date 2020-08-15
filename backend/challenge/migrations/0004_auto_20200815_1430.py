# Generated by Django 3.1 on 2020-08-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_auto_20200814_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challenge',
            options={'default_permissions': [], 'ordering': ['index']},
        ),
        migrations.RemoveConstraint(
            model_name='exprflag',
            name='unique_flag',
        ),
        migrations.AddConstraint(
            model_name='exprflag',
            constraint=models.UniqueConstraint(fields=('user', 'sub_challenge'), name='unique_flag_for_every_user'),
        ),
    ]
