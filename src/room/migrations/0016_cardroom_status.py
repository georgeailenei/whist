# Generated by Django 4.1.1 on 2023-01-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0015_stats_cards_in_play"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardroom",
            name="status",
            field=models.CharField(default="Waiting", max_length=15),
        ),
    ]
