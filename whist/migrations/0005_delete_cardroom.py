# Generated by Django 4.1.1 on 2022-10-19 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whist', '0004_alter_player_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardRoom',
        ),
    ]
