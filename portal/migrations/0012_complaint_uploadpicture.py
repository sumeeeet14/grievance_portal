# Generated by Django 3.2.5 on 2021-07-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_complaint_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='uploadpicture',
            field=models.ImageField(default='images/default', upload_to='images'),
        ),
    ]
