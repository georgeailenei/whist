# Generated by Django 4.1.1 on 2023-01-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0004_user_registration_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="points",
            field=models.IntegerField(default=1000),
        ),
    ]
