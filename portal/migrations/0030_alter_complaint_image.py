# Generated by Django 3.2.5 on 2021-08-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0029_alter_complaint_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='articles'),
        ),
    ]
