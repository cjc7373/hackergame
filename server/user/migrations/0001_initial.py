# Generated by Django 2.1.12 on 2019-10-04 09:32

from django.db import migrations, models
import server.user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(unique=True)),
                ('hash', models.TextField(default=server.user.models.gen_hash)),
                ('group', models.TextField()),
                ('nickname', models.TextField(null=True)),
                ('name', models.TextField(null=True)),
                ('sno', models.TextField(null=True)),
                ('tel', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('token', models.TextField()),
            ],
            options={
                'permissions': [('full', '管理个人信息')],
                'default_permissions': (),
            },
        ),
    ]
