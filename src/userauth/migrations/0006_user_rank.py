# Generated by Django 4.1.1 on 2023-02-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_user_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
