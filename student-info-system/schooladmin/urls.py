from django.urls import path

from . import views

app_name = 'schooladmin'
urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('user/<int:userid>/change_password', views.user_change_password, name='change_password'),
    path('user/<int:userid>/edit', views.user_edit, name='user_edit'),
    path('user/<int:userid>', views.user, name='user'),
    path('student/<int:userid>', views.student, name='student'),
    path('professor/<int:userid>', views.professor, name='professor'),
    path('professor/<int:userid>/items', views.professor_items, name='professor_items'),
    path('professor/<int:userid>/item_new', views.professor_item_new, name='professor_item_new'),
    path('professor/<int:userid>/item/<int:item_id>', views.professor_item,
         name='professor_item'),
    path('user_new', views.user_new, name='user_new'),
    path('students', views.students, name='students'),
    path('majors', views.majors, name='majors'),
    path('major/<int:majorid>/edit', views.major_edit, name='major_edit'),
    path('major/<int:majorid>', views.major, name='major'),
    path('major_new', views.major_new, name='major_new'),
    path('courses', views.courses, name='courses'),
    path('course/<int:courseid>/edit', views.course_edit, name='course_edit'),
    path('course/<int:courseid>/section_new', views.course_section_new,
         name='course_section_new'),
    path('course/<int:courseid>', views.course, name='course'),
    path('course_new', views.course_new, name='course_new'),
    path('sections', views.sections, name='sections'),
    path('section/<int:sectionid>/refreshitems',
         views.section_refreshitems,
         name='section_refreshitems'),
    path('section/<int:sectionid>/edit', views.section_edit, name='section_edit'),
    path('section/<int:sectionid>/new_from_section',
         views.section_new_from_section,
         name='section_new_from_section'),
    path('section/<int:sectionid>/students_manage',
         views.section_students_manage,
         name='section_students_manage'),
    path('section/<int:sectionid>', views.section, name='section'),
    path('section_new', views.section_new, name='section_new'),
    path('sectionstudent/<int:id>', views.sectionstudent, name='sectionstudent'),
    path('semesters', views.semesters, name='semesters'),
    path('semester_new', views.semester_new, name='semester_new'),
    path('semester/<int:semester_id>/section_new',
         views.semester_section_new,
         name='semester_section_new'),
    path('semester/<int:semester_id>/edit', views.semester_edit, name='semester_edit'),
    path('semester/<int:semester_id>', views.semester, name='semester'),
    path('student/<int:userid>/transcript', views.transcript, name='transcript'),
    path('demographics', views.demographics, name='demographics'),
    path('messages', views.usermessages, name='messages'),
    path('message/<int:id>', views.message, name='message'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile', views.profile, name='profile'),
]
