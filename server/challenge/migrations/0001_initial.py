# Generated by Django 2.1.12 on 2019-10-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('category', models.TextField()),
                ('enabled', models.BooleanField()),
                ('detail', models.TextField()),
                ('url', models.TextField(null=True)),
                ('prompt', models.TextField(null=True)),
                ('index', models.IntegerField(db_index=True)),
                ('flags', models.TextField()),
            ],
            options={
                'ordering': ['index'],
                'permissions': [('full', '管理题目')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Expr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_index', models.IntegerField()),
                ('expr', models.TextField(db_index=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Challenge')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ExprFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expr', models.TextField(db_index=True)),
                ('user', models.IntegerField(db_index=True)),
                ('flag', models.TextField(db_index=True)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(unique=True)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='exprflag',
            unique_together={('expr', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='expr',
            unique_together={('challenge', 'flag_index')},
        ),
    ]
