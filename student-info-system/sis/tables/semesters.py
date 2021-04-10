import django_tables2 as tables

from sis.models import Semester
from sis.tables import *


class SemestersTable(tables.Table):
    semester = ClassyColumn(verbose_name='Semester',
                            css_class_base='semester',
                            accessor='name',
                            order_by=('semester_order'))
    session = ClassyColumn(verbose_name='Session',
                           css_class_base='session',
                           accessor='session',
                           order_by=('session_order'))
    year = ClassyColumn(css_class_base='year')
    date_registration_opens = ClassyColumn(verbose_name='Registration Opens',
                                           css_class_base='date')
    date_registration_closes = ClassyColumn(verbose_name='Registration Closes',
                                            css_class_base='date')
    date_last_drop = ClassyColumn(verbose_name='Date of Last Drop', css_class_base='date')
    date_started = ClassyColumn(verbose_name='Start of Classes', css_class_base='date')
    date_ended = ClassyColumn(verbose_name='End of Classes', css_class_base='date')

    class Meta:
        model = Semester
        template_name = "django_tables2/bootstrap.html"
        fields = ('semester', 'session', 'year', 'date_registration_opens',
                  'date_registration_closes', 'date_started', 'date_last_drop', 'date_ended')
        attrs = {"class": 'semester_table'}
        row_attrs = {'class': 'semester_row', 'data-id': lambda record: record.pk}


class SemestersSummaryTable(tables.Table):
    year = ClassyColumn(verbose_name='Year', css_class_base='year')
    session = ClassyColumn(verbose_name='Semester',
                           css_class_base='session',
                           accessor='name',
                           order_by=('semester_order'))

    class Meta:
        model = Semester
        template_name = "django_tables2/bootstrap.html"
        fields = (
            'year',
            'session',
        )
        attrs = {"class": 'semester_table'}
        row_attrs = {'class': 'semester_row', 'data-id': lambda record: record.pk}