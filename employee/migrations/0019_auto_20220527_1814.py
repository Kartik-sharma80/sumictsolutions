# Generated by Django 3.1.2 on 2022-05-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_auto_20220527_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
