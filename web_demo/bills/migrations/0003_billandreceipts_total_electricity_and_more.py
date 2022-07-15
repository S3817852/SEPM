# Generated by Django 4.0.4 on 2022-07-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_alter_billandreceipts_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billandreceipts',
            name='total_electricity',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='billandreceipts',
            name='total_water',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
