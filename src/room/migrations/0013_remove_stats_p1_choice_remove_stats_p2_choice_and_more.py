# Generated by Django 4.1.1 on 2022-12-21 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0012_stats_p1_choice_stats_p2_choice_stats_p3_choice_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stats",
            name="p1_choice",
        ),
        migrations.RemoveField(
            model_name="stats",
            name="p2_choice",
        ),
        migrations.RemoveField(
            model_name="stats",
            name="p3_choice",
        ),
        migrations.RemoveField(
            model_name="stats",
            name="p4_choice",
        ),
    ]