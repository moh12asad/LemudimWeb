from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Student,Teacher,StudentsInClass,category, Contact,MessageToTeacher,ClassNotice ,StudentMarks,ClassFile
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(StudentMarks)
admin.site.register(Teacher)
admin.site.register(StudentsInClass)
admin.site.register(category)
admin.site.register(Contact)
admin.site.register(ClassNotice)
admin.site.register(MessageToTeacher)
admin.site.register(ClassFile)