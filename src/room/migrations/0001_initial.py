# Generated by Django 4.1.1 on 2022-11-12 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CardRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("seats", models.CharField(default="Available", max_length=15)),
                ("players_count", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Stats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("board", models.CharField(blank=True, max_length=20)),
                ("trump_card", models.CharField(blank=True, max_length=10)),
                ("team_one_score", models.IntegerField(default=0)),
                ("team_two_score", models.IntegerField(default=0)),
                ("player_position", models.IntegerField(default=0)),
                ("played_card", models.CharField(blank=True, max_length=4)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="room.cardroom"
                    ),
                ),
            ],
        ),
    ]
