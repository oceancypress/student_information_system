# Generated by Django 3.1.7 on 2021-04-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0003_auto_20210415_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicprobationtask',
            name='frequency_type',
            field=models.CharField(choices=[(None, 'immediate'), ('interval', 'interval'), ('date', 'date')], max_length=8, verbose_name='Frequency Type'),
        ),
        migrations.AlterField(
            model_name='interval',
            name='interval_type',
            field=models.CharField(choices=[('seconds', 'seconds'), ('weeks', 'weeks'), ('hours', 'hours'), ('months', 'months'), ('days', 'days'), ('minutes', 'minutes')], max_length=7, verbose_name='Interval Type'),
        ),
    ]