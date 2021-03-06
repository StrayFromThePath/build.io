# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Felials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('felial_name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'db_table': 'felials',
                'verbose_name': '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_number', models.CharField(max_length=45, verbose_name='\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('felial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Felials', verbose_name='\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435')),
            ],
            options={
                'db_table': 'machines',
                'verbose_name': '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='MachinesTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type_name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u0430 \u0442\u0435\u0445\u043d\u0438\u043a\u0438')),
            ],
            options={
                'db_table': 'machines_types',
                'verbose_name': '\u0422\u0438\u043f \u0442\u0435\u0445\u043d\u0438\u043a\u0438',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0442\u0435\u0445\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0443\u0447\u0430\u0441\u0442\u043a\u0430')),
                ('spot_address', models.CharField(max_length=100, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('felial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Felials', verbose_name='\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435')),
            ],
            options={
                'db_table': 'spots',
                'verbose_name': '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0443\u0447\u0430\u0441\u0442\u043e\u043a',
                'verbose_name_plural': '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0443\u0447\u0430\u0441\u0442\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0440\u0438\u0433\u0430\u0434\u044b')),
                ('felial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Felials', verbose_name='\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435')),
                ('spot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Spots', verbose_name='\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0443\u0447\u0430\u0441\u0442\u043e\u043a')),
            ],
            options={
                'db_table': 'teams',
                'verbose_name': '\u0411\u0440\u0438\u0433\u0430\u0434\u0430',
                'verbose_name_plural': '\u0411\u0440\u0438\u0433\u0430\u0434\u044b',
            },
        ),
        migrations.AddField(
            model_name='machines',
            name='machine_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.MachinesTypes', verbose_name='\u0422\u0438\u043f \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='machines',
            name='spot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Spots', verbose_name='\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0443\u0447\u0430\u0441\u0442\u043e\u043a'),
        ),
    ]
