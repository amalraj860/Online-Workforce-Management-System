# Generated by Django 4.2.5 on 2023-10-27 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application_form',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='application_form',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
