# Generated by Django 4.1.1 on 2022-12-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0009_stats_p1_choice_stats_p2_choice_stats_p3_choice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardroom",
            name="game_status",
            field=models.BooleanField(default=False),
        ),
    ]
