# Generated by Django 4.2.5 on 2023-09-26 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date_publicacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='counteudo',
            new_name='conteudo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='sutitulo',
            new_name='subtitulo',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 26, 17, 28, 34, 768526, tzinfo=datetime.timezone.utc)),
        ),
    ]
