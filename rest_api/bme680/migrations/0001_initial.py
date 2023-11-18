# Generated by Django 4.2.7 on 2023-11-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BME680',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('gas', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'BME680',
                'verbose_name_plural': 'BME680',
                'ordering': ['-time'],
            },
        ),
    ]
