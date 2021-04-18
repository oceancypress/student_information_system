# Generated by Django 3.1.7 on 2021-04-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0004_auto_20210415_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicprobationtask',
            name='title',
            field=models.CharField(blank=True, max_length=30, verbose_name='Task Title'),
        ),
        migrations.AlterField(
            model_name='academicprobationtask',
            name='frequency_type',
            field=models.CharField(choices=[('interval', 'interval'), (None, 'immediate'), ('date', 'date')], max_length=8, verbose_name='Frequency Type'),
        ),
        migrations.AlterField(
            model_name='interval',
            name='interval_type',
            field=models.CharField(choices=[('days', 'days'), ('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours'), ('weeks', 'weeks'), ('months', 'months')], max_length=7, verbose_name='Interval Type'),
        ),
    ]