# Generated by Django 4.1.1 on 2022-12-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0002_user_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="choice",
            field=models.IntegerField(default=0),
        ),
    ]
