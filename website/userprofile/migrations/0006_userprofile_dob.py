# Generated by Django 3.2 on 2021-05-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20210524_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
