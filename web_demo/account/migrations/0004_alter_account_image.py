# Generated by Django 4.0.4 on 2022-06-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rentcontract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='default_user.png', upload_to='profile_pics'),
        ),
    ]