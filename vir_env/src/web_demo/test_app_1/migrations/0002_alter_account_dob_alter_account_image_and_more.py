# Generated by Django 4.0.4 on 2022-06-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='DoB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_Owner',
            field=models.BooleanField(),
        ),
    ]
