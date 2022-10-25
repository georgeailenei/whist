# Generated by Django 4.1.1 on 2022-10-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='hand',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='played_cards',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='tricks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
