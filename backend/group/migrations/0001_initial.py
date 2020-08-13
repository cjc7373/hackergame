# Generated by Django 3.1 on 2020-08-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_message', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('rejected', 'rejected'), ('pending', 'pending'), ('deleted', 'deleted')], default='pending', max_length=10)),
            ],
            options={
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('rule_has_phone_number', models.BooleanField()),
                ('rule_has_email', models.BooleanField()),
                ('rule_email_suffix', models.CharField(blank=True, max_length=50, null=True)),
                ('rule_has_name', models.BooleanField()),
                ('rule_must_be_verified_by_admin', models.BooleanField()),
                ('apply_hint', models.TextField(blank=True, verbose_name='给申请者的提示')),
                ('verified', models.BooleanField(default=False, verbose_name='是否为认证过的组')),
                ('verify_message', models.TextField(blank=True)),
            ],
            options={
                'default_permissions': [],
            },
        ),
    ]