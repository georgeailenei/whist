# Generated by Django 4.1.1 on 2022-12-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="choice",
            field=models.BooleanField(default=None),
        ),
    ]
