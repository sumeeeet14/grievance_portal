# Generated by Django 3.2.5 on 2021-07-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_alter_complaint_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='upload_picture',
            field=models.ImageField(default='images/default', upload_to='images'),
        ),
    ]
