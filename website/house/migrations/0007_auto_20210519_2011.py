# Generated by Django 3.2 on 2021-05-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_auto_20210519_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rental_fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='tenant_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]