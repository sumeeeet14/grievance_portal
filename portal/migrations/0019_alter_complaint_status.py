# Generated by Django 3.2.5 on 2021-07-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0018_auto_20210725_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='Complaint Has Been Submitted.', max_length=200),
        ),
    ]
