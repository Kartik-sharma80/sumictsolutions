# Generated by Django 3.1.2 on 2022-05-27 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_auto_20220527_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='date',
        ),
    ]
