# Generated by Django 3.2 on 2021-05-19 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_house_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('Rented_rooms', 'Rented_rooms'), ('Empty_rooms', 'Empty_rooms')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=100)),
                ('rental_fee', models.IntegerField()),
                ('status', models.CharField(choices=[('Rented', 'Rented'), ('Empty', 'Empty')], max_length=255, null=True)),
                ('house_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
        ),
    ]
