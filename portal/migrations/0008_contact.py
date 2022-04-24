# Generated by Django 3.2.5 on 2021-07-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20210714_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Department', models.CharField(max_length=10)),
                ('Mobile', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=30)),
                ('Reason', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
