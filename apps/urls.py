from django.urls import path
from .views import *
urlpatterns=[
    path('',login_view,name='login'),
    path('admin_dash/',admin_dash,name='admin_dash'),
    path('school_admin/',school_admin,name='school_admin'),
    path('principal_dash/',principal_dash,name='principal_dash'),
    path('school_principal/',register_view,name='school_principal'),
    path('add_subject/',subject_view,name='add_subject'),
    path('add_class/',class_view,name='add_class'),
    path('update_class/<str:pk>/',update_class,name='update_class'),
    path('delete_class/<str:pk>/',delete_class,name='delete_class'),
    path('update_subject/<str:pk>/',update_subject,name='update_subject'),
    path('delete_subject/<str:pk>/',delete_subject,name='delete_subject'),
    path('register_student/',student_view,name='register_student'),
    path('update_student/<str:pk>/',update_student,name='update_student'),
    path('delete_student/<str:pk>/',delete_student,name='delete_student'),
    path('logout',logout_view,name='logout'),
    path('staff_student_summary/',staff_student,name='staff_student_summary'),
    path('academic/',academic_dash,name='academic'),
    path('dashboard/',teacher_dash,name='dashboard'),
    path('student/',student,name='student'),
    path('teacher/',teacher_views,name='teacher'),
    path('subject_teacher/',subject_teacher,name='subject_teacher'),
    path('update_subject_teacher/<str:pk>/',update_subject_teacher,name='update_subject_teacher'),
    path('delete_subject_teacher/<str:pk>/',delete_subject_teacher,name='delete_subject_teacher'),

    path('upload_score/',upload_score,name='upload_score'),
    path('leave_permision/',leave_permission,name='leave_permission'),
    path('student_detail/',student_detail,name='student_detail'),
    path('student_result/',student_result, name='student_result'),
    path('permission_response/',permission_response, name='permission_response'),
    path('permission_detail/<str:pk>/',permission_detail,name='permission_detail'),
    path('modify_roles/<str:pk>/',modify_roles,name='modify_roles'),
    path('update_staff/<str:pk>/',update_staff,name='update_staff'),

    path('delete_staff/<str:pk>/',delete_staff,name='delete_staff'),
    path('report/', generate_report, name='generate_report'),
    path('find_teacher/', find_teacher, name='find_teacher'),





    



]
