# Generated by Django 3.2.5 on 2021-07-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_complaint_regarding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
