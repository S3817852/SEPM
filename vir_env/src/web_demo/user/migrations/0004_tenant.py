# Generated by Django 4.0.4 on 2022-04-24 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('is_rented', models.BooleanField(default=False, null=True)),
                ('tenant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
    ]
