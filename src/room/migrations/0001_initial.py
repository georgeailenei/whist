# Generated by Django 4.1.1 on 2022-12-02 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('seats', models.CharField(default='Available', max_length=15)),
                ('players_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(blank=True, max_length=20)),
                ('old_board', models.CharField(blank=True, max_length=20)),
                ('trump_card', models.CharField(blank=True, max_length=10)),
                ('team_one_score', models.IntegerField(default=0)),
                ('team_two_score', models.IntegerField(default=0)),
                ('player_position', models.IntegerField(default=0)),
                ('played_card', models.CharField(blank=True, max_length=4)),
                ('cards_per_round', models.IntegerField(default=0)),
                ('winner', models.CharField(blank=True, max_length=40)),
                ('timer', models.DateTimeField(auto_now=True)),
                ('last_played_card', models.DateTimeField()),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='room.cardroom')),
            ],
        ),
    ]
