from django import forms
from django.contrib.auth.forms import UserCreationForm
from classroom.models import User, Teacher, Student, StudentMsg, MessageToTeacher, ClassNotice, ClassFile, SubmitFile
from django.db import transaction


class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'answer'}),
            'password1': forms.PasswordInput(attrs={'class': 'answer'}),
            'password2': forms.PasswordInput(attrs={'class': 'answer'}),
        }


class TeacherProfileForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name', 'subject_name', 'phone', 'email', 'money_per_hour', 'description', 'rate', 'payment_way',
                  'schedule']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'answer'}),
            'subject_name': forms.TextInput(attrs={'class': 'answer'}),
            'phone': forms.NumberInput(attrs={'class': 'answer'}),
            'money_per_hour': forms.NumberInput(attrs={'class': 'answer'}),
            'description': forms.TextInput(attrs={'class': 'answer'}),
            'email': forms.EmailInput(attrs={'class': 'answer'}),
            'payment_way': forms.TextInput(attrs={'class': 'answer'}),
            'schedule': forms.TextInput(attrs={'class': 'answer'}),

        }


class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name', 'subject_name', 'email', 'phone', 'teacher_profile_pic', 'money_per_hour']


class StudentProfileForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name', 'language', 'phone', 'email', 'student_of']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'answer'}),
            'language': forms.TextInput(attrs={'class': 'answer'}),
            'phone': forms.NumberInput(attrs={'class': 'answer'}),
            'email': forms.EmailInput(attrs={'class': 'answer'}),
            'student_of': forms.TextInput(attrs={'class': 'answer'}),
        }


class StudentProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name', 'language', 'email', 'phone', 'student_of', 'student_profile_pic']


class MsgForm(forms.ModelForm):
    class Meta():
        model = StudentMsg
        fields = ['subject_name', 'msg_obtained']


class MessageForm(forms.ModelForm):
    class Meta():
        model = MessageToTeacher
        fields = ['message']


class NoticeForm(forms.ModelForm):
    class Meta():
        model = ClassNotice
        fields = ['message']


class FileForm(forms.ModelForm):
    class Meta():
        model = ClassFile
        fields = ['file_name', 'file']


class SubmitForm(forms.ModelForm):
    class Meta():
        model = SubmitFile
        fields = ['submit']
