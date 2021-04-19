import django_tables2 as tables

from sis.models import SectionReferenceItem
from sis.tables import *


class SectionReferenceItemsTable(tables.Table):
    section = ClassyColumn(css_class_base='section')
    semester = ClassyColumn(accessor='section__semester', css_class_base='semester')
    professor = ClassyColumn(accessor='section__professor', css_class_base='user_name')
    index = ClassyColumn(verbose_name="#", css_class_base='item_index')
    type = ClassyColumn(verbose_name='Type', css_class_base='item_type', accessor='item__type')
    title = ClassyColumn(css_class_base='item_title', accessor='item__title')
    link = tables.TemplateColumn(
        '{% if record.item.link %}<a href="{{record.item.link}}" target="_blank">' +
        '{{record.item.link}}</a>{% endif %}')
    edition = ClassyColumn(css_class_base='item_edition', accessor='item__edition')
    description = ClassyColumn(css_class_base='item_description', accessor='item__description')

    class Meta:
        template_name = "django_tables2/bootstrap.html"
        fields = ('semester', 'section', 'professor', 'index', 'type', 'title', 'edition',
                  'description', 'link')
        row_attrs = {'class': 'secitem_row', 'data-id': lambda record: record.pk}
        attrs = {"class": 'secitems_table'}


class ReferenceItemsForSectionTable(SectionReferenceItemsTable):

    class Meta:
        template_name = "django_tables2/bootstrap.html"
        exclude = ('section', 'semester', 'professor')
        row_attrs = {'class': 'secitem_row', 'data-id': lambda record: record.pk}
        attrs = {"class": 'secitems_table'}
