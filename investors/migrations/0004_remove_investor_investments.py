# Generated by Django 3.1.7 on 2021-03-27 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0003_auto_20210327_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='investments',
        ),
    ]
