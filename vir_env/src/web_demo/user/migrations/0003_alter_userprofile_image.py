# Generated by Django 4.0.4 on 2022-04-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userprofile_dob_remove_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default_user.jpg', upload_to='profile_pics'),
        ),
    ]