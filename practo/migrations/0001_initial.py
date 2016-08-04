# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('locality', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('timings', models.TextField(max_length=128)),
                ('full_address', models.TextField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('speciality', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=128)),
                ('fees', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=7)),
                ('locality', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('experience', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clinic',
            name='doctors',
            field=models.ManyToManyField(to='practo.Doctors'),
            preserve_default=True,
        ),
    ]
