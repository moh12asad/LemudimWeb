from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns = [
    path('signup/', views.SignUp, name="signup"),
    path('signup/student_signup/', views.StudentSignUp, name="StudentSignUp"),
    path('signup/teacher_signup/', views.TeacherSignUp, name="TeacherSignUp"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name="student_detail"),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name="teacher_detail"),
    path('update/student/<int:pk>/', views.StudentUpdateView, name="student_update"),
    path('update/teacher/<int:pk>/', views.TeacherUpdateView, name="teacher_update"),
    path('student/<int:pk>/enter_msg', views.add_msg, name="enter_msg"),
    path('student/<int:pk>/msg_list', views.student_msg_list, name="student_msg_list"),
    path('msg/<int:pk>/update', views.update_msg, name="update_msg"),
    path('student/<int:pk>/add', views.add_student.as_view(), name="add_student"),
    path('student_added/', views.student_added, name="student_added"),
    path('students_list/', views.students_list, name="students_list"),
    path('teachers_list/', views.teachers_list, name="teachers_list"),
    path('teacher/class_students_list', views.class_students_list, name="class_student_list"),
    path('student/<int:pk>/all_msg', views.StudentAllMsgList.as_view(), name="all_msg_list"),
    path('student/<int:pk>/message', views.write_message, name="write_message"),
    path('teacher/<int:pk>/messages_list', views.messages_list, name="messages_list"),
    path('teacher/write_notice', views.add_notice, name="write_notice"),
    path('student/<int:pk>/class_notice', views.class_notice, name="class_notice"),
    path('upload_file/', views.upload_file, name="upload_file"),
    path('class_file/', views.class_file, name="class_file"),
    path('file_list/', views.file_list, name="file_list"),
    path('update_file/<int:id>/', views.update_file, name="update_file"),
    path('file_delete/<int:id>/', views.file_delete, name="file_delete"),
    path('submit_file/<int:id>/', views.submit_file, name="submit_file"),
    path('submit_list/', views.submit_list, name="submit_list"),
    path('change_password/', views.change_password, name="change_password"),
    path('contact/', views.contact, name="contact"),
]
