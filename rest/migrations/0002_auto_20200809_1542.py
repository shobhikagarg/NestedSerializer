# Generated by Django 2.0 on 2020-08-09 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.ForeignKey(default='India', on_delete=django.db.models.deletion.CASCADE, to='rest.Country'),
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.ManyToManyField(default='Rajasthan', related_name='persons', to='rest.State'),
        ),
        migrations.AddField(
            model_name='person',
            name='town',
            field=models.CharField(default='Gangashaher', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_country', to='rest.Country'),
        ),
    ]