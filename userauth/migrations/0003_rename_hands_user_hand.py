# Generated by Django 4.1.1 on 2022-10-31 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_user_played_hand_user_tricks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hands',
            new_name='hand',
        ),
    ]
