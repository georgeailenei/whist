# Generated by Django 4.1.1 on 2022-10-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardroom',
            name='status',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
    ]
