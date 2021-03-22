from django.urls import path, include

from . import views

app_name = 'schooladmin'
urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('user/<int:userid>/change_password', views.user_change_password, name='change_password'),
    path('user/<int:userid>/edit', views.user_edit, name='user_edit'),
    path('user/<int:userid>', views.user, name='user'),
    path('user_new', views.user_new, name='user_new'),
    path('majors', views.majors, name='majors'),
    path('major/<str:abbreviation>/edit', views.major_edit, name='major_edit'),
    path('major/<str:abbreviation>', views.major, name='major'),
    path('major_new', views.major_new, name='major_new'),
    path('courses', views.courses, name='courses'),
    path('course/<int:courseid>/edit', views.course_edit, name='course_edit'),
    path('course/<int:courseid>', views.course, name='course'),
    path('course_new', views.course_new, name='course_new'),
    path('semesters', views.semesters, name='semesters'),
    path('semester/<int:semester_id>', views.semester, name='semester'),
    path('new_semester', views.new_semester, name='new_semester'),
]
