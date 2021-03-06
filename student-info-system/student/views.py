from datetime import date

from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import redirect, render, reverse

from sis.authentication_helpers import role_login_required
from sis.models import (Course, Section, Profile, Semester, SectionStudent, Message,
                        SemesterStudent)

from sis.utils import filtered_table2, DUMMY_ID

from sis.elements.course import CoursesTable, MajorCoursesMetTable, RequirementsCourseFilter
from sis.elements.major import MajorSelectForm, MajorChangeForm
from sis.elements.section import SectionFilter
from sis.elements.sectionreferenceitem import SectionReferenceItemsTable, SectionItemFilter
from sis.elements.sectionstudent import (StudentHistoryTable, StudentHistoryFilter,
                                         DropRequestForm)
from sis.elements.semester import SemestersSummaryTable, SemesterFilter


@role_login_required(Profile.ACCESS_STUDENT)
def index(request):
    return current_schedule_view(request)
    # data = {
    #     'current_semester': Semester.current_semester(),
    #     'registration_open': Semester.semesters_open_for_registration(),
    # }
    # data.update(request.user.profile.unread_messages())
    # return render(request, 'student/home_student.html', data)


@role_login_required(Profile.ACCESS_STUDENT)
def current_schedule_view(request):
    current_semester = Semester.current_semester()
    context = {
        'my_sections':
            request.user.profile.student.sectionstudent_set.filter(
                section__semester=current_semester),
        'name':
            request.user.profile.name,
        'semester':
            current_semester,
    }
    return render(request, 'student/current_schedule.html', context)


@role_login_required(Profile.ACCESS_STUDENT)
def registration_view(request):
    has_filter = None
    student = request.user.profile.student
    # If the student has to register for semesters first, do this:
    # semester_list = student.semesters.order_by('-date_started')
    # if semester_list.count() == 0:
    #     return HttpResponse("You are not registered for any semesters.")
    # If the student can register for anything open, do this:
    semester_list = Semester.objects.filter(
        date_registration_opens__lte=date.today(),
        date_registration_closes__gte=date.today()).order_by('-date_started')
    context = {'student': student, 'semesters': semester_list}

    if request.method == 'POST':
        qs = semester_list.filter(id=request.POST.get('semester'))
        if qs.count() == 1:
            the_sem = qs.get()
            context['semester'] = the_sem.id
            the_sections = the_sem.section_set.exclude(students=student)
            filt = SectionFilter(request.GET, queryset=the_sections)
            has_filter = any(field in request.GET for field in set(filt.get_fields()))
            context['sections'] = filt.qs
            context['any_sections'] = filt.qs.count() != 0

            if request.POST.get('register') is not None:
                any_selected = False

                for sect in filt.qs:
                    # indicate student is attending this semester...
                    sem = SemesterStudent.objects.filter(student=student, semester=sect.semester)
                    if sem.count() < 1:
                        SemesterStudent.objects.create(student=student, semester=sect.semester)

                    course_val = request.POST.get(str(sect.course.id))
                    if course_val is not None and int(course_val) == sect.id:
                        if not Course.objects.get(id=sect.course.id).prerequisites_met(student):
                            messages.error(
                                request,
                                f'You have not met the prerequisites for {sect.course.name}.')
                        elif sect.course.graduate and not student.grad_student:
                            messages.error(request,
                                           f'{sect.course.name} is a graduate-level class.')
                        else:
                            status = SectionStudent.REGISTERED
                            if sect.seats_remaining < 1:
                                status = SectionStudent.WAITLISTED
                            sectstud = SectionStudent(section=sect,
                                                      student=student,
                                                      status=status)
                            sectstud.save()
                            sect.is_selected = True
                            messages.success(request, f'Registration for {sect.name} successful.')
    else:
        if len(semester_list) > 0:
            the_sem = semester_list[0]
            context['semester'] = the_sem.id
            the_sections = the_sem.section_set.exclude(students=student)
            filt = SectionFilter(request.GET, queryset=the_sections)
            has_filter = any(field in request.GET for field in set(filt.get_fields()))
            context['sections'] = filt.qs
            context['any_sections'] = the_sections.count() != 0
        else:
            context['any_sections'] = 0

    if has_filter is not None:
        context['has_filter'] = has_filter
        context['filter'] = filt
    # signal template that this entry is a different course from last section
    last_course = None
    if 'sections' in context:
        for sect in context['sections']:
            sect.new_course = sect.course != last_course
            if sect.new_course:
                last_course = sect.course

    return render(request, 'student/registration.html', context)


@role_login_required(Profile.ACCESS_STUDENT)
def history(request):
    the_user = request.user
    student = the_user.profile.student
    ssects = student.sectionstudent_set.all().order_by('section__semester',
                                                       'section__course__name')
    semesters = []
    accumulating_sem = {
        'semester': None,
    }
    for ssect in ssects:
        if ssect.section.semester != accumulating_sem['semester']:
            if accumulating_sem['semester'] is not None:
                semesters.append(accumulating_sem)
            accumulating_sem = {
                'semester':
                    ssect.section.semester,
                'gpa':
                    student.semesterstudent_set.get(semester=ssect.section.semester).gpa,
                'sections': [],
                'credits_earned':
                    student.semesterstudent_set.get(semester=ssect.section.semester
                                                    ).credits_earned,
            }
        accumulating_sem['sections'].append(ssect)

    data = {
        'auser': the_user,
        'semesters': semesters,
    }

    remaining = the_user.profile.student.requirements_met_list()
    stats = remaining.filter(met=False).aggregate(remaining_course_count=Count('id'),
                                                  remaining_credit_count=Sum('credits_earned'))
    if stats['remaining_credit_count'] is None:
        stats['remaining_credit_count'] = 0

    data.update(stats)

    data.update(
        filtered_table2(
            name='majorcourses',
            qs=remaining,
            filter=RequirementsCourseFilter,
            table=MajorCoursesMetTable,
            request=request,
            self_url=reverse('student:history'),
            click_url=reverse('schooladmin:course', args=[DUMMY_ID]),
        ))
    return render(request, 'student/history.html', data)


@role_login_required(Profile.ACCESS_STUDENT)
def drop(request, id):
    the_user = request.user
    ssect = SectionStudent.objects.get(id=id)

    if request.method == 'POST':
        drop_form = DropRequestForm(request.POST,
                                    sectionstudent_qs=the_user.profile.student.droppable_classes(
                                        semester=ssect.section.semester))
        if drop_form.is_valid():
            the_ssect = drop_form.cleaned_data.get('student_section')
            reason = drop_form.cleaned_data.get('reason')
            mesg = the_user.profile.student.request_drop(sectionstudent=the_ssect, reason=reason)
            as_str = mesg.time_sent.strftime('%m/%d/%Y, %H:%M:%S')
            messages.success(request, f'Request submitted at {as_str}.')
            return redirect(reverse('sis:profile'))
        else:
            messages.error(request, "Something went wrong.")

    droppable = the_user.profile.student.droppable_classes(semester=ssect.section.semester)
    drop_form = DropRequestForm(
        initial={
            'student_section': ssect,
        },
        sectionstudent_qs=droppable,
    )
    data = {
        'auser': the_user,
        'count': droppable.count(),
        'drop_form': drop_form,
    }
    return render(request, 'student/drop.html', data)


@role_login_required(Profile.ACCESS_STUDENT)
def secitems(request):
    the_user = request.user

    the_semester = Semester.current_semester()
    if request.method == 'POST':
        the_id = request.POST.get('semester', the_semester.id)
        the_semester = Semester.objects.get(id=the_id)

    data = {
        'auser': the_user,
        'semester': the_semester,
        'semesters': the_user.profile.student.semesters.all(),
    }

    data.update(
        filtered_table2(
            name='secitems',
            qs=the_user.profile.student.section_reference_items_for(the_semester),
            filter=SectionItemFilter,
            table=SectionReferenceItemsTable,
            request=request,
            self_url=reverse('student:secitems'),
            click_url=reverse('sis:secitem', args=[DUMMY_ID]),
        ))

    return render(request, 'student/items.html', data)


@role_login_required(Profile.ACCESS_STUDENT)
def test_majors(request):
    the_user = request.user
    the_major = the_user.profile.student.major

    if request.method == 'POST':
        major_form = MajorSelectForm(request.POST)
        if major_form.is_valid():
            the_major = major_form.cleaned_data.get('major')
        else:
            messages.error(request, "Something went wrong")
    else:
        major_form = MajorSelectForm(initial={
            'major': the_major,
        })

    data = {
        'auser': the_user,
        'major': the_major,
        'major_form': major_form,
    }
    candidate_remaining = the_user.profile.student.requirements_met_list(major=the_major)
    stats = candidate_remaining.filter(met=False).aggregate(
        remaining_course_count=Count('id'), remaining_credit_count=Sum('credits_earned'))
    if stats['remaining_credit_count'] is None:
        stats['remaining_credit_count'] = 0
    data.update(stats)

    data.update(
        filtered_table2(
            name='majorcourses',
            qs=candidate_remaining,
            filter=RequirementsCourseFilter,
            table=MajorCoursesMetTable,
            request=request,
            self_url=reverse('student:test_majors'),
            click_url=reverse('schooladmin:course', args=[DUMMY_ID]),
        ))

    return render(request, 'student/test_majors.html', data)


@role_login_required(Profile.ACCESS_STUDENT)
def request_major_change(request):
    the_user = request.user

    if request.method == 'POST':
        major_form = MajorChangeForm(request.POST)
        if major_form.is_valid(
        ) and major_form.cleaned_data.get('major') != the_user.profile.student.major:
            the_major = major_form.cleaned_data.get('major')
            reason = major_form.cleaned_data.get('reason')
            mesg = the_user.profile.student.request_major_change(major=the_major, reason=reason)
            as_str = mesg.time_sent.strftime('%m/%d/%Y, %H:%M:%S')
            messages.success(request, f'Request submitted at {as_str}.')
            return redirect(reverse('sis:profile'))
        else:
            messages.error(request, "Please select a major other than your current one.")

    the_major = the_user.profile.student.major
    data = {
        'auser': the_user,
        'major': the_major,
        'major_form': MajorChangeForm(initial={
            'major': the_major,
        }),
    }
    return render(request, 'student/change_major.html', data)


@role_login_required(Profile.ACCESS_STUDENT)
def request_transcript(request):
    the_user = request.user

    mesg = Message.objects.create(
        sender=the_user.profile,
        recipient=the_user.profile.student.major.contact,
        message_type=Message.TRANSCRIPT_REQUEST_TYPE,
        subject="Transcript Request",
        support_data={
            'student': the_user.profile.student.pk,
        },
    )
    as_str = mesg.time_sent.strftime('%m/%d/%Y, %H:%M:%S')
    messages.success(request, f'Request submitted at {as_str}.')
    return redirect(reverse('sis:profile'))
