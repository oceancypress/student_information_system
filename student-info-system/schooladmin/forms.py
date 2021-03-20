from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sis.models import Major, Semester, UpperField, CharField, IntegerField, DateField

ROLE_CHOICES = (
    ('Student', 'Student'),
    ('Professor', 'Professor'),
    ('Admin', 'Admin'),
)


class UpperFormField(forms.CharField):

    def clean(self, value):
        supa_clean = super().clean(value)
        return str(supa_clean).upper()


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, help_text='Select type of user')
    major = forms.ModelChoiceField(queryset=None, required=False)

    class Meta:
        model = User
        fields = ('role', 'username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', 'major')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # this may be necessary: applyClassConfig2FormControl(self)
        self.fields['major'].queryset = Major.objects.all()


class MajorCreationForm(forms.ModelForm):
    abbreviation = UpperFormField(max_length=6, help_text='Abbreviation')
    name = forms.CharField(max_length=256)
    description = forms.CharField(max_length=256, required=False)

    class Meta:
        model = Major
        fields = ('abbreviation', 'name', 'description')


SEASON = (('FALL', 'Fall'), ('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('WINTER', 'Winter'))


class SemesterCreationForm(forms.Form):
    semester = CharField(max_length=6, choices=SEASON, default='FA')
    year = IntegerField(default=2000)
    date_started = DateField(auto_now=False)
    date_ended = DateField(auto_now=False)
    date_registration_opens = DateField(auto_now=False)
    date_last_drop = DateField(auto_now=False)

    class Meta:
        model = Semester
        fields = ('semester', 'year', 'date_started', 'date_ended', 'date_registration_opens',
                  'date_last_drop')


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, help_text='Select type of user')
    major = forms.ModelChoiceField(queryset=None, required=False)

    class Meta:
        model = User
        fields = ('role', 'first_name', 'last_name', 'email', 'major')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        # this may be necessary: applyClassConfig2FormControl(self)
        self.fields['major'].queryset = Major.objects.all()
