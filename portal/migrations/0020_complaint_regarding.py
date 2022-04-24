# Generated by Django 3.2.5 on 2021-07-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_alter_complaint_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='regarding',
            field=models.CharField(choices=[('CLG', 'College'), ('HOS', 'Hostel')], default='CLG', max_length=10),
        ),
    ]
