# Generated by Django 3.1.7 on 2021-04-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0016_auto_20210415_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval',
            name='interval_type',
            field=models.CharField(choices=[('hours', 'hours'), ('weeks', 'weeks'), ('minutes', 'minutes'), ('days', 'days'), ('seconds', 'seconds'), ('months', 'months')], max_length=7, verbose_name='Interval Type'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='date_ended',
            field=models.DateField(help_text='Must be on or after Classes Start', verbose_name='Classes End'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='date_last_drop',
            field=models.DateField(help_text='Must be on or after Classes Start and before Classes End', verbose_name='Last Drop'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='date_registration_closes',
            field=models.DateField(help_text='Must be on or after Registration Opens', verbose_name='Registration Closes'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='date_started',
            field=models.DateField(help_text='Must on or after Registration Opens', verbose_name='Classes Start'),
        ),
    ]