# Generated by Django 4.1.1 on 2022-10-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameStats',
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
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hand', models.CharField(max_length=50)),
                ('tricks', models.IntegerField()),
                ('played_cards', models.CharField(max_length=50)),
            ],
        ),
    ]
