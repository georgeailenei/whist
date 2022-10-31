# Generated by Django 4.1.1 on 2022-10-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_alter_stats_player_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='board',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stats',
            name='played_card',
            field=models.CharField(blank=True, default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stats',
            name='player_position',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='team_one_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='team_two_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='trump_card',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
