from django.test import TestCase

# Create your tests here.
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
import reverse
# TODO: Configure your database in settings.py and sync before running tests.

class Test_lemudim(TestCase):

    def test_home(self):

        class SignUpPageTests(TestCase):
            def TeacherSignUp(self) -> None:
                self.username = 'testuser'
                self.email = 'testuser@email.com'
                self.age = 20
                self.password = 'password'

            def test_signup_page_url(self):
                response = self.client.get("/users/signup/")
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name='signup.html')

            def test_signup_page_view_name(self):
                response = self.client.get(reverse('signup'))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name='signup.html')

            def test_signup_form(self):
                response = self.client.post(reverse('signup'), data={
                    'username': self.username,
                    'email': self.email,
                    'age': self.age,
                    'password1': self.password,
                    'password2': self.password
                })
                self.assertEqual(response.status_code, 200)

                users = get_user_model().objects.all()
                self.assertEqual(users.count(), 1)