# Generated by Django 2.0 on 2017-12-09 22:46

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20171209_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_size',
            field=image_cropping.fields.ImageRatioField('src', '450x550', adapt_rotation=False, allow_fullsize=True, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='profile size'),
        ),
    ]
