# Generated by Django 2.1.12 on 2019-09-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0004_auto_20181011_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='backend',
            field=models.TextField(choices=[('ustc', '中国科学技术大学'), ('zju', '浙江大学'), ('nju', '南京大学'), ('njust', '南京理工大学'), ('hnu', '湖南大学'), ('uestc', '电子科学技术大学'), ('sjtu', '上海交通大学'), ('eduemail', '其他高校'), ('email', '其他'), ('sms', '其他')], db_index=True),
        ),
    ]