# Generated by Django 3.2.5 on 2021-08-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
