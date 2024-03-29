# Generated by Django 4.1.5 on 2023-01-27 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('number_car', models.TextField()),
                ('color', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StateNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_place', models.PositiveIntegerField()),
                ('time_start', models.DateTimeField(auto_now_add=True)),
                ('time_stop', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.car', verbose_name='Модель авто')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.driver', verbose_name='Собственик')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='driver_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.driver', verbose_name='Водитель машины'),
        ),
    ]
