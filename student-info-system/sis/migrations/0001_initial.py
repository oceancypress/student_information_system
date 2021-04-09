# Generated by Django 3.1.7 on 2021-04-09 06:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_number', models.CharField(max_length=20, verbose_name='Number')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='Description')),
                ('credits_earned', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Credits')),
            ],
            options={
                'ordering': ['major', 'catalog_number', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', sis.models.UpperField(max_length=6, verbose_name='Abbreviation')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='Description')),
                ('courses_required', models.ManyToManyField(blank=True, related_name='required_by', to='sis.Course')),
            ],
            options={
                'ordering': ['abbreviation'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.major')),
            ],
            options={
                'ordering': ['profile__user__username'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('A', 'Admin'), ('P', 'Professor'), ('S', 'Student')], default='S', max_length=1)),
                ('bio', models.CharField(blank=True, max_length=256)),
                ('demo_age', models.CharField(blank=True, choices=[('Under 18', 'Under 18'), ('18-21', '18-21'), ('22-25', '22-25'), ('26-30', '26-30'), ('31-40', '31-40'), ('41-54', '41-54'), ('55-64', '55-64'), ('65 or over', '65 or over'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_race', models.CharField(blank=True, choices=[('White/Caucasian', 'White/Caucasian'), ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander'), ('Hispanic', 'Hispanic'), ('Black', 'Black'), ('American Indian/Alaska Native', 'American Indian/Alaska Native'), ('Decline to State', 'Decline to State')], max_length=40)),
                ('demo_gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans'), ('Other', 'Other'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_employment', models.CharField(blank=True, choices=[('Full Time Student', 'Full Time Student'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Unemployed/Seeking', 'Unemployed/Seeking'), ('Retired', 'Retired'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_income', models.CharField(blank=True, choices=[('Under $40K', 'Under $40K'), ('$40K-$80K', '$40K-$80K'), ('$80K-$150K', '$80K-$150K'), ('$150K+', '$150K+'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_education', models.CharField(blank=True, choices=[('partial High School', 'partial High School'), ('High School Diploma', 'High School Diploma'), ('college without degree awarded', 'college without degree awarded'), ('Associates', 'Associates'), ('College Bachelors', 'College Bachelors'), ('Masters', 'Masters'), ('Doctorate', 'Doctorate'), ('Decline to State', 'Decline to State')], max_length=35)),
                ('demo_orientation', models.CharField(blank=True, choices=[('Heterosexual', 'Heterosexual'), ('Lesbian/Gay', 'Lesbian/Gay'), ('Bisexual', 'Bisexual'), ('Other', 'Other'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_marital', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_disability', models.CharField(blank=True, choices=[('None', 'None'), ('Physical', 'Physical'), ('Emotional', 'Emotional'), ('Mental', 'Mental'), ('Other', 'Other'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_veteran', models.CharField(blank=True, choices=[('None', 'None'), ('Veteran', 'Veteran'), ('Decline to State', 'Decline to State')], max_length=20)),
                ('demo_citizenship', models.CharField(blank=True, choices=[('United States', 'United States'), ('US Permanent Resident', 'US Permanent Resident'), ('Visa', 'Visa'), ('Other', 'Other'), ('Decline to State', 'Decline to State')], max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
        migrations.CreateModel(
            name='ReferenceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('link', models.CharField(blank=True, max_length=256, null=True, verbose_name='Link')),
                ('edition', models.CharField(blank=True, max_length=256, null=True, verbose_name='Edition')),
                ('type', models.CharField(choices=[('req', 'Required'), ('opt', 'Optional'), ('rec', 'Recommended'), ('syl', 'Syllabus'), ('ass', 'Assignment')], default='req', max_length=3, verbose_name='Type')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.professor')),
            ],
            options={
                'unique_together': {('course', 'professor', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Section Number')),
                ('capacity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Capacity')),
                ('location', models.CharField(max_length=256, verbose_name='Location')),
                ('hours', models.CharField(max_length=256, verbose_name='Hours')),
                ('status', models.CharField(choices=[('Closed', 'Closed'), ('Open', 'Open'), ('In Progress', 'In Progress'), ('Grading', 'Grading'), ('Graded', 'Graded'), ('Cancelled', 'Cancelled')], default='Closed', max_length=20, verbose_name='Section Status')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.professor')),
            ],
            options={
                'ordering': ['semester', 'course', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_registration_opens', models.DateField(verbose_name='Registration Opens')),
                ('date_registration_closes', models.DateField(verbose_name='Registration Closes')),
                ('date_started', models.DateField(verbose_name='Classes Start')),
                ('date_last_drop', models.DateField(verbose_name='Last Drop')),
                ('date_ended', models.DateField(verbose_name='Classes End')),
                ('session', models.CharField(choices=[('FA', 'Fall'), ('WI', 'Winter'), ('SP', 'Spring'), ('SU', 'Summer')], default='FA', max_length=6, verbose_name='semester')),
                ('year', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2300)], verbose_name='year')),
            ],
            options={
                'ordering': ['date_started'],
                'unique_together': {('session', 'year')},
            },
        ),
        migrations.CreateModel(
            name='SemesterStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.semester')),
            ],
            options={
                'ordering': ['semester', 'student'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.major')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sis.profile')),
                ('semesters', models.ManyToManyField(related_name='semester_students', through='sis.SemesterStudent', to='sis.Semester')),
            ],
            options={
                'ordering': ['profile__user__username'],
            },
        ),
        migrations.AddField(
            model_name='semesterstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.student'),
        ),
        migrations.CreateModel(
            name='SectionStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.SmallIntegerField(blank=True, choices=[(4, 'A'), (3, 'B'), (2, 'C'), (1, 'D'), (0, 'F')], default=None, null=True)),
                ('status', models.CharField(choices=[('Registered', 'Registered'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Graded', 'Graded'), ('Drop Requested', 'Drop Requested'), ('Dropped', 'Dropped')], default='Registered', max_length=20, verbose_name='Student Status')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.section')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student')),
            ],
            options={
                'ordering': ['section', 'student'],
                'unique_together': {('section', 'student')},
            },
        ),
        migrations.AddField(
            model_name='section',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.semester'),
        ),
        migrations.AddField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(related_name='section_students', through='sis.SectionStudent', to='sis.Student'),
        ),
        migrations.AddField(
            model_name='professor',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sis.profile'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField(editable=False, verbose_name='Sent at')),
                ('time_read', models.DateTimeField(blank=True, null=True, verbose_name='Read at')),
                ('time_archived', models.DateTimeField(blank=True, null=True, verbose_name='Archived at')),
                ('subject', models.CharField(max_length=256)),
                ('body', models.TextField(blank=True, null=True)),
                ('high_priority', models.BooleanField(default=False)),
                ('in_response_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.message')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_to', to='sis.profile', verbose_name='Recipient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_by', to='sis.profile', verbose_name='Sender')),
            ],
            options={
                'ordering': ['time_sent'],
            },
        ),
        migrations.AddField(
            model_name='major',
            name='professors',
            field=models.ManyToManyField(blank=True, related_name='prof', to='sis.Professor'),
        ),
        migrations.CreateModel(
            name='CoursePrerequisite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_course', to='sis.course')),
                ('prerequisite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_prerequisite', to='sis.course')),
            ],
            options={
                'ordering': ['course', 'prerequisite'],
                'unique_together': {('course', 'prerequisite')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.major'),
        ),
        migrations.AddField(
            model_name='course',
            name='prereqs',
            field=models.ManyToManyField(through='sis.CoursePrerequisite', to='sis.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='semesterstudent',
            unique_together={('semester', 'student')},
        ),
        migrations.CreateModel(
            name='SectionReferenceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=1, verbose_name='#')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.referenceitem')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.section')),
            ],
            options={
                'unique_together': {('section', 'item'), ('section', 'index')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('course', 'semester', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('major', 'catalog_number')},
        ),
    ]
