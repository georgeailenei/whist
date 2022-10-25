# Generated by Django 4.1.1 on 2022-10-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0013_alter_cardroom_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=20)),
                ('trump_card', models.CharField(max_length=10)),
                ('team_one_score', models.IntegerField()),
                ('team_two_score', models.IntegerField()),
                ('player_position', models.IntegerField()),
                ('played_card', models.CharField(max_length=4)),
            ],
        ),
    ]
