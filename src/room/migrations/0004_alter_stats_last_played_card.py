# Generated by Django 4.1.1 on 2022-12-06 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_stats_last_played_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='last_played_card',
            field=models.DateTimeField(),
        ),
    ]
