# Generated by Django 3.1.7 on 2021-04-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0019_auto_20210417_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicprobationtask',
            name='frequency_type',
            field=models.CharField(choices=[('immediate', 'immediate'), ('date', 'date'), ('interval', 'interval')], max_length=9, verbose_name='Frequency Type'),
        ),
        migrations.AlterField(
            model_name='interval',
            name='interval_type',
            field=models.CharField(choices=[('months', 'months'), ('minutes', 'minutes'), ('hours', 'hours'), ('seconds', 'seconds'), ('days', 'days'), ('weeks', 'weeks')], max_length=7, verbose_name='Interval Type'),
        ),
    ]