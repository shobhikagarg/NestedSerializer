# Generated by Django 2.0 on 2020-08-09 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20200809_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
    ]
