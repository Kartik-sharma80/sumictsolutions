# Generated by Django 3.1.2 on 2022-04-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20220424_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetail',
            name='image',
        ),
    ]
