# Generated by Django 4.1.1 on 2022-10-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_alter_cardroom_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardroom',
            name='seats',
            field=models.CharField(default='Available', max_length=10),
        ),
    ]
