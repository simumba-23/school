from django.shortcuts import render,redirect,get_object_or_404
from django .http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import logging
from .forms import *
from .models import *
import pandas as pd


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'Academic Master':
                return redirect('academic')
            elif user.role == 'School Admin':
                return redirect('admin_dash')
            elif user.role == 'School Principal':
                return redirect('principal_dash')
            elif user.role == 'Teacher':
                return redirect('dashboard')
            elif user.role == 'Student':
                return redirect('student')
    
        else:
            error_message = 'Invalid username or password.Try again!'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
#@login_required(login_url=('login'))

def register_view(request):
    queryset=CustomUser.objects.exclude(is_superuser=True)
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.password = make_password(str(request.POST['password']))
            get_form.save()
            return redirect('school_principal')
                    
    context={
        'form':UserRegisterForm,
        'queryset':queryset
    }
    return render(request,'principal/user_registration.html',context)
def academic_home(request):
    return render(request,'academic/index.html')
class SubjectAlreadyExists(Exception):
    pass
def subject_view(request):
    form=SubjectCreateForm(request.POST)
    query=Subject.objects.all()
    if form.is_valid():
        try:
            name = form.cleaned_data.get('name')
            code = form.cleaned_data.get('code')
            if Subject.objects.filter(name=name,code=code).exists():
                raise SubjectAlreadyExists(f"Subject with name '{name}' and '{code}' already exists.")
            form.save()
            messages.success(request,f"Subject '{name}' and '{code}' added Succesfully")

            
        except SubjectAlreadyExists as e:
            messages.err or(request,str(e))

        return redirect('add_subject')
    # else:
    #     messages.error(request, "Form is not valid. Please check the inputs.")
    
    context={
        'query':query,
        'form':SubjectCreateForm,
    }
    return render(request,'academic/add_subject.html',context)

class ClassAlreadyExists(Exception):
    pass

def class_view(request):
    form=ClassCreateForm(request.POST)
    queries=Class.objects.all()
    if form.is_valid():
        try:
            name = form.cleaned_data.get('name')
            if Class.objects.filter(name=name).exists():
                raise ClassAlreadyExists(f"Class with name '{name}' already exists.")
            
            form.save()
            messages.success(request,f"class '{name}' added succesfully" )
            return redirect('add_class')

        except ClassAlreadyExists as e:
            messages.error(request,str(e))
        

    context={
        'form':ClassCreateForm,
        'queries':queries
    }
    return render(request,'academic/add_class.html',context)
def update_class(request,pk):
    update_class = Class.objects.get(id=pk)
    form=ClassCreateForm(instance=update_class)
    if request.method == "POST":
        form = ClassCreateForm(request.POST,instance=update_class)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            messages.success(request,f"class '{name}' updated succesfully" )
            form.save()

            return redirect('add_class')
    context = {
        'form':form,
    }
    return render(request,'academic/update_class.html',context)

def delete_class(request,pk):
    delete_item = Class.objects.get(id=pk)
    if request.method == 'POST':

        delete_item.delete()
        messages.success(request,f"class '{delete_item.name}' deleted succesfully")
        return redirect('add_class')
    return render(request,'academic/delete_class.html')
def update_student(request,pk):
    student_update = CustomUser.objects.get(id=pk)
    form = StudentUpdateForm(instance=student_update)
    if request.method == 'POST':
        form =StudentUpdateForm(request.POST,instance=student_update)
        if form.is_valid():
            form.save()
            return redirect('register_student')
    else:
        StudentUpdateForm()
    context = {
        'form':form
    }

    return render(request,'academic/update_student.html',context)
def delete_student(request,pk):
    delete_item = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        delete_item.delete()
        return redirect('register_student')
    return render(request,'academic/delete_student.html')
def update_subject(request,pk):
    subject_update =Subject.objects.get(id=pk)
    form = SubjectCreateForm(instance=subject_update)
    if request.method == 'POST':
        form = SubjectCreateForm(request.POST,instance=subject_update)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            form.save()
            messages.success(request,f"Subject '{name}' updated succesfully" )
            return redirect('add_subject')
    context = {
        'form':form,
    }

        
    return render(request,'academic/update_subject.html',context)

def delete_subject(request,pk):
    delete_item = Subject.objects.get(id=pk)
    if request.method == 'POST':
        delete_item.delete()
        messages.success(request,f"class '{delete_item.name}' deleted succesfully" )
        return redirect('add_subject')
    return render(request,'academic/delete_subject.html')

def student_view(request):
    user=StudentRegistrationForm()
    student_profile=StudentCreateForm()
    # student_detail=CustomUser.objects.filter(role='Student')
 
    queryset= Student.objects.all()
    if request.method == "POST":
        student_profile=StudentCreateForm(request.POST)
        user=StudentRegistrationForm(request.POST)
        if user.is_valid() and student_profile.is_valid(): 
            get_user=user.save(commit=False)
            get_user.role = 'Student'
            get_user.password = make_password(str(request.POST['password']))
            get_user.save() 
            get_student=student_profile.save(commit=False)
            get_student.user = get_user
            get_student.save()
            return redirect('register_student')
    context={
        'user':user,
        'student_profile':student_profile,
        'queryset':queryset,
        # 'student_detail':student_detail

    }

    
    return render(request,'academic/register_student.html',context)

def student_detail(request):
    return render(request,'student/index.html')
def student_result(request):
    student_id = request.user.id
    student_scores = Score.objects.filter(student_id=student_id)
    context = {
        'student_scores':student_scores
    }
    return render(request,'student/student_result.html',context)
def  update_staff(request,pk):
    get_staff = get_object_or_404(CustomUser,id=pk)
    form = UserRegisterForm(instance=get_staff)

    if request.method == 'POST':
        form = UserRegisterForm(request.POST,instance=get_staff)
        if form.is_valid():
            form.save()
            messages.success(request,'Staff is updated succesfuly')

    context = {
        'form': form
    }
    return render(request,'principal/staff_updates.html',context)

def subject_teacher(request):
    queryset = TeacherSubject.objects.all()
    if request.method=='POST':
        form = SubjectTeacherForm(request.POST)
        if form.is_valid():
            form.save()       
    else:
        form = SubjectTeacherForm
    context = {
        'form':form,
        'queryset':queryset,
    }
    return render(request,'academic/teacher_assign_form.html',context)
def update_subject_teacher(request,pk):
    update_item = get_object_or_404(TeacherSubject, id=pk)
    form = SubjectTeacherForm(instance=update_item)
    if request.method == 'POST':
        form = SubjectTeacherForm(request.POST,instance=update_item)
        if form.is_valid():
            form.save()
            return redirect('subject_teacher')
    else:
        form = SubjectTeacherForm(instance=update_item)
    context = {
        'form':form
    }
    
    return render(request,'academic/update_student.html',context)
def delete_subject_teacher(request,pk):
    delete_item = get_object_or_404(TeacherSubject,id=pk) 
    if request.method == 'POST':
        delete_item.delete()
        return redirect('subject_teacher')
    return render(request,'academic/delete_student.html')
def staff_student(request):
    queryset= Student.objects.count()
    # query=Student.objects.filter(sex='Male').count()
    # querys=Student.objects.filter(sex='Female').count()
    staff_q1=CustomUser.objects.count()
    staff_q2=CustomUser.objects.filter(sex='Male').count()
    staff_q3=CustomUser.objects.filter(sex='Female').count()
    context={
        'queryset': queryset,
        'staff_q1':staff_q1,
        'staff_q2':staff_q2,
        'staff_q3':staff_q3,
    }
    return render(request,'principal/registration_summary.html',context)
def academic_dash(request):
    
    return render(request,'academic/home.html')
def principal_dash(request):
    
    return render(request,'principal/home.html')
def student(request):
    
    return render(request,'student/home.html')

def admin_dash(request):
    
    return render(request,'school_admin/home.html')
def school_admin(request):
    queryset=CustomUser.objects.exclude(is_superuser=True)
    context= {
        'queryset':queryset,
    }

    return render(request,'school_admin/staff_list.html',context)


def teacher_dash(request):

    return render(request,'teachers/home.html')
def teacher_views(request):
    user_id = request.user.id
    queryset=TeacherSubject.objects.filter(user_id=user_id)
    context={
            'queryset':queryset
        }
    
    return render(request,'teachers/teach.html',context)

def upload_score(request):
    if request.method == 'POST':
        form = ScoreUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_data = request.FILES['excel_file']
            df = pd.read_excel(excel_data)

            # Get the user who submitted the data
            submitting_user = request.user  # Assuming user authentication is enabled

            # Process and save data to database
            for index, row in df.iterrows():
                # Extract data from DataFrame
                student= row['student']
                subject_name = row['subject']
                marks = row['marks']
                rank = row['grade']

                # Get or create Student instance
                student, created = CustomUser.objects.get_or_create(role='Student',student=student)

                # Get or create Subject instance
                subject, created = Subject.objects.get_or_create(name=subject_name)

                # Create Score instance and associate with the submitting user and student
                Score.objects.create(
                    user=submitting_user,
                    student=student,
                    subject=subject,
                    marks=marks,
                    grade=rank,
                )

            return render(request, 'teachers/success.html')
    else:
        form = ScoreUploadForm()
    return render(request, 'teachers/score_upload_form.html', {'form': form})
def leave_permission(request):
    permission_status = Permission.objects.filter(user=request.user)
    form = PermissionForm()

    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('dashboard')
    else:
        form = PermissionForm()
    context = {
            'form':form,
            'permission_status':permission_status
        }
    return render(request,'teachers/permission.html',context)
def permission_response(request):
    permission_query = Permission.objects.all()
    context = {
        'permission_query':permission_query

    }
    return render(request,'principal/permission_response.html',context)
def permission_detail(request,pk):
    get_detail = Permission.objects.get(id=pk)
    form = PermissionForm(instance=get_detail)
    if request.method == "POST":
        form = PermissionForm(request.POST,instance=get_detail)
        if form.is_valid():
            form.save()
            return redirect('permission_detail')

    

    return render (request,'principal/permission_detail.html')

def delete_staff(request,pk):
    get_user = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        get_user.delete()
        return redirect('admin_dash')
    return render(request,'school_admin/delete_page.html')

def modify_roles(request,pk):
    modify_user = CustomUser.objects.get(id=pk)
    form = ModifyRoleForm(instance=modify_user)
    if request.method =="POST":
        form = ModifyRoleForm(request.POST,instance=modify_user)
        if form.is_valid():
            form.save()
            return redirect('admin_dash')
    context = {
        'form':form
    }
    return render(request,'school_admin/update_roles.html',context)
def teacher_office(request):

    return render(request,'academic/teacher_office.html')


from django.db.models import Sum
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle


def generate_report(request):
    # Retrieve the authenticated student
    student = request.user

    # Retrieve all subjects
    subjects = Subject.objects.all()
    subject_names = {subject.id: subject.name for subject in subjects}

    # Retrieve scores for the student
    scores = Score.objects.filter(student=student)

    # Calculate the total marks for the student
    total_marks = sum(int(score.marks) for score in scores)

    # Calculate the average score for each subject
    subject_averages = {}
    for subject in subjects:
        subject_scores = scores.filter(subject=subject)
        if subject_scores.exists():
            subject_averages[subject.name] = sum(int(score.marks) for score in subject_scores) / subject_scores.count()
        else:
            subject_averages[subject.name] = 0

    # Calculate the rank of the student among all students based on total marks
    all_students = CustomUser.objects.filter(role='Student')
    ranked_students = all_students.annotate(total_marks=Sum('score__marks')).order_by('-total_marks').values_list('id', flat=True)
    rank = list(ranked_students).index(student.id) + 1

    # Create PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.first_name}_report.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add rank information
    rank_paragraph = Paragraph(f'Position: {rank}', style=ParagraphStyle(name='RankStyle', alignment=1))
    elements.append(rank_paragraph)

    name_paragraph = Paragraph(f'Student Name: {student.first_name} {student.last_name}', style=ParagraphStyle(name='NameStyle', alignment=1))
    elements.append(name_paragraph)

    # Prepare data for the table
    data = [['Subject', 'Marks', 'Grade', 'Average']]
    for subject in subjects:
        score = scores.filter(subject=subject).first()
        if score:
            data.append([subject.name, score.marks, score.grade, subject_averages[subject.name]])
        else:
            data.append([subject.name, '-', '-', subject_averages[subject.name]])

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Add table to elements
    elements.append(table)

    # Build PDF document
    doc.build(elements)
    return response

from django.db.models import Q
def find_teacher(request):
    query = request.GET.get('query','')
    results = []
    if query:
        results = CustomUser.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)|
            Q(office__name__icontains=query) |       
            Q(office__office_number__icontains=query) 
        )

    context = {
        'results': results,
    }
    return render(request,'student/find_teacher.html',context)