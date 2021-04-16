# Generated by Django 3.1.7 on 2021-04-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0012_auto_20210415_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicprobationtask',
            name='frequency_type',
            field=models.CharField(choices=[(None, 'immediate'), ('date', 'date'), ('interval', 'interval')], max_length=8, verbose_name='Frequency Type'),
        ),
        migrations.AlterField(
            model_name='interval',
            name='interval_type',
            field=models.CharField(choices=[('minutes', 'minutes'), ('days', 'days'), ('months', 'months'), ('weeks', 'weeks'), ('hours', 'hours'), ('seconds', 'seconds')], max_length=7, verbose_name='Interval Type'),
        ),
    ]
