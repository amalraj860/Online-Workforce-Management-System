# Generated by Django 4.2.5 on 2023-11-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_signup',
            name='status',
            field=models.CharField(default='Active', max_length=50, null=True),
        ),
    ]
