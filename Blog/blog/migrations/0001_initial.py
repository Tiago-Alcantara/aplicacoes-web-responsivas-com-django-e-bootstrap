# Generated by Django 4.2.5 on 2023-09-20 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('sutitulo', models.CharField(max_length=255)),
                ('counteudo', models.TextField()),
                ('date_publicacao', models.DateTimeField(default=datetime.datetime(2023, 9, 20, 16, 40, 22, 905489))),
            ],
        ),
    ]
