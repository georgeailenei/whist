# Generated by Django 4.1.1 on 2022-10-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='Cool', max_length=30),
            preserve_default=False,
        ),
    ]
