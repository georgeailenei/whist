# Generated by Django 4.1.1 on 2023-03-14 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0025_remove_cardroom_remaining_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardroom',
            name='players_count',
        ),
    ]
