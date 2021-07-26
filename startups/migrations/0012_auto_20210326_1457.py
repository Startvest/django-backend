# Generated by Django 3.1.7 on 2021-03-26 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0011_auto_20210326_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='startups.startup'),
        ),
        migrations.AlterField(
            model_name='startupgallery',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='startups.startup'),
        ),
    ]
