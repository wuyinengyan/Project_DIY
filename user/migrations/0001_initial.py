# Generated by Django 2.2.5 on 2019-12-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('create_datetime', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
