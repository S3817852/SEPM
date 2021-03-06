# Generated by Django 3.2 on 2021-05-25 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0008_alter_conversationmessage_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile')),
            ],
        ),
    ]
