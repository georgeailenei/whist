# Generated by Django 4.1.1 on 2023-03-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0026_remove_cardroom_players_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardroom',
            name='players_count',
            field=models.IntegerField(default=0),
        ),
    ]