# Generated by Django 4.1.1 on 2022-10-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_alter_cardroom_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardroom',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
