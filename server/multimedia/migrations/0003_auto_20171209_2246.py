# Generated by Django 2.0 on 2017-12-09 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0002_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profileimage',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
    ]
