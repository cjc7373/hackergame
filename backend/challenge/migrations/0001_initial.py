# Generated by Django 3.1 on 2020-08-12 12:11

import dirtyfields.dirtyfields
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
                ('index', models.IntegerField(db_index=True, verbose_name='顺序')),
                ('name', models.TextField(unique=True)),
                ('category', models.TextField()),
                ('detail', models.TextField(help_text='会被放入 div 的 HTML，其中的 {token} 会被替换为 URL encode 后的用户 token', verbose_name='题目描述')),
                ('prompt', models.TextField(blank=True, verbose_name='提示')),
            ],
            options={
                'ordering': ['index'],
                'permissions': [('full', '管理题目'), ('view', '查看题目')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SubChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, help_text='若只有一个子题则不填')),
                ('score', models.SmallIntegerField()),
                ('enabled', models.BooleanField(help_text='\n        设为无效的题目不会被看到，也不会产生任何分数。 将题目改为无效时，它产生的分数会被移除，但并不删除此前的提交记录。\n        将题目改为有效时，此前的提交记录会重新产生分数。\n        <em>注意：在比赛开始后修改此项信息会重算排行榜，产生较大开销。</em>\n        ')),
                ('flag_type', models.CharField(choices=[('expr', 'a Python expression'), ('text', 'plain text')], max_length=5)),
                ('flag', models.TextField(help_text="\n        若 flag 类型为表达式, 则填写一个 Python 表达式，其计算结果为 flag。 示例：\n        'flag{' + md5('secret' + token)[:16] + '}'。 可以使用的变量及函数： token, base64, md5, sha1, sha224,\n        sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512\n        ")),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_challenge', to='challenge.challenge')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='ExprFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.TextField()),
                ('sub_challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.subchallenge')),
            ],
            options={
                'default_permissions': [],
            },
        ),
    ]
