# Generated by Django 4.1.1 on 2023-02-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]