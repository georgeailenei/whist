# Generated by Django 4.1.1 on 2022-10-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whist', '0003_remove_player_player_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestats',
            name='played_card',
            field=models.CharField(default=None, max_length=3),
            preserve_default=False,
        ),
    ]