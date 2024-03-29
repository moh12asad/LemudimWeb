from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
import misaka


# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Student')
    name = models.CharField(max_length=250)
    student_of = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    student_profile_pic = models.ImageField(upload_to="classroom/student_profile_pic", blank=True)

    def get_absolute_url(self):
        return reverse('classroom:student_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['language']


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Teacher')
    name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    money_per_hour = models.CharField(max_length=250)
    teacher_profile_pic = models.ImageField(upload_to="classroom/teacher_profile_pic", blank=True)
    class_students = models.ManyToManyField(Student, through="StudentsInClass")
    rate=models.IntegerField()
    description = models.TextField()
    payment_way=models.CharField(max_length=250)
    schedule=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('classroom:teacher_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class StudentMsg(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='given_msg', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="msg", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=250)
    msg_obtained = models.TextField()

    def __str__(self):
        return self.subject_name


class StudentsInClass(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="class_teacher", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="user_student_name", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ('teacher', 'student')


class MessageToTeacher(models.Model):
    student = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['student', 'message']


class ClassNotice(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='class_notice')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['teacher', 'message']


class ClassFile(models.Model):
    student = models.ManyToManyField(Student, related_name='student_file')
    teacher = models.ForeignKey(Teacher, related_name='teacher_file', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=250)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ['-created_at']


class SubmitFile(models.Model):
    student = models.ForeignKey(Student, related_name='student_submit', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='teacher_submit', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    submitted_file = models.ForeignKey(ClassFile, related_name='submission_for_file',
                                       on_delete=models.CASCADE)
    submit = models.FileField(upload_to='Submission')

    def __str__(self):
        return "Submitted" + str(self.submitted_file.file_name)

    class Meta:
        ordering = ['-created_at']


class category(models.Model):
    course = models.CharField(max_length=50)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name + ", subject: " + self.subject
