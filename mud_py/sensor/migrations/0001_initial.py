# Generated by Django 3.1.7 on 2021-03-10 20:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controlnode', '0001_initial'),
        ('zone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensorID', models.CharField(max_length=100)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
                ('controlnode', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='controlnode.controlnode')),
                ('zone', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='zone.zone')),
            ],
        ),
        migrations.CreateModel(
            name='SensorDataUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviatedName', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SensorDataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=50)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.sensordataunit')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('value', models.FloatField()),
                ('datatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.sensordatatype')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('sensor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor.sensor')),
            ],
        ),
    ]
