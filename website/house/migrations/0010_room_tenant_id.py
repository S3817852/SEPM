# Generated by Django 3.2 on 2021-05-25 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_alter_conversationmessage_options'),
        ('house', '0009_auto_20210520_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='tenant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile'),
        ),
    ]
