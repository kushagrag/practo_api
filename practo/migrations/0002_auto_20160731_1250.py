# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timings', models.TextField(max_length=128)),
                ('clinic', models.ForeignKey(to='practo.Clinic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
        migrations.AddField(
            model_name='doctor_clinic',
            name='doctor',
            field=models.ForeignKey(to='practo.Doctor'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='doctors',
        ),
    ]
