from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from sis.models import (Admin, Course, CoursePrerequisite, Major, Professor, Section,
                        SectionStudent, Semester, SemesterStudent, Student, TranscriptRequest,
                        UpperField)


class AdminUserViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(AdminUserViews, cls).setUpTestData()
        AdminUserViews.u1 = User.objects.create_user(username='u1', password='hello')
        Admin.objects.create(user=AdminUserViews.u1)

    # list views
    def test_users_view_exists(self):
        login = self.client.login(username='u1', password='hello')
        response = self.client.get('/schooladmin/users')
        self.assertEqual(response.status_code, 200)

    # single-object views
    def test_user_view_exists(self):
        login = self.client.login(username='u1', password='hello')
        response = self.client.get('/schooladmin/user/1')
        self.assertEqual(response.status_code, 200)

    # edit views
    def test_edit_user_view_exists(self):
        login = self.client.login(username='u1', password='hello')
        response = self.client.get('/schooladmin/user/1/edit')
        self.assertEqual(response.status_code, 200)

    # create views
    def test_new_user_view_exists(self):
        login = self.client.login(username='u1', password='hello')
        response = self.client.get('/schooladmin/user_new')
        self.assertEqual(response.status_code, 200)

    # misc
    def test_user_pass_change_view_exists(self):
        login = self.client.login(username='u1', password='hello')
        response = self.client.get('/schooladmin/user/1/change_password')
        self.assertEqual(response.status_code, 200)
