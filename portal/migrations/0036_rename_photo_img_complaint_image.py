# Generated by Django 3.2.5 on 2021-08-06 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0035_auto_20210806_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='photo_img',
            new_name='image',
        ),
    ]
