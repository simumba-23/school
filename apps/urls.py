from django.urls import path
from .views import *
urlpatterns=[
    path('',login_view,name='login'),
    path('school_principal/',register_view,name='school_principal'),
    path('add_subject/',subject_view,name='add_subject'),
    path('add_class/',class_view,name='add_class'),
    path('register_student/',student_view,name='register_student'),
    path('school_admin/',admin_view,name='school_admin'),
    path('logout',logout_view,name='logout'),
    path('staff_student/',staff_student,name='staff_student'),
    path('teacher/',teacher_view,name='teacher')
]
