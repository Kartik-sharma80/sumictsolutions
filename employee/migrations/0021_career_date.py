# Generated by Django 3.1.2 on 2022-05-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_remove_career_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='date',
            field=models.DateField(null=True),
        ),
    ]