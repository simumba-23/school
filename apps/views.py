from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import *
from .models import *

# Create your views here.
def login_view(request):
    if request.method=='POST':
        UserLoginForm(request.POST or None)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
      
        if user is not None and user.role=='Academic Teacher':
            login(request,user)
            return redirect('add_class')
        elif user is not None and user.role=='School Admin':
            login(request,user)
            return redirect('school_admin')
        elif user is not None and user.role=='School Principal':
            print('principle')
            login(request,user)
            return redirect('school_principal')
        elif user is not None and user.role=='teacher':
            login(request,user)
            return redirect('teacher')   
        else:
            messages.success(request,"incorect Password or Username")
            return redirect('login')
        
        
    context={
        'form':UserLoginForm
    }  
    return render(request,'login.html',context)
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required(login_url=('login'))

def register_view(request):
    queryset=User.objects.all()
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
    return render(request,'registeration_report.html',context)


def subject_view(request):
    form=SubjectCreateForm(request.POST)
    query=Subject.objects.all()
    if form.is_valid():
        form.save()
        return redirect('add_subject')
    else:
        messages.success(request,"something please contact admin")
    
    context={
        'query':query,
        'form':SubjectCreateForm,
    }
    return render(request,'add_subject.html',context)

def class_view(request):
    form=ClassCreateForm(request.POST)
    queries=Class.objects.all()
    if form.is_valid():
        get_form=form.save(commit=False)
        get_form.save()
        return redirect('add_class')
    else:
        msg='something wrong'
    
    context={
        'form':ClassCreateForm,
        'queries':queries
    }
    return render(request,'add_class.html',context)

def student_view(request):
    form=StudentCreateForm(request.POST)
    queryset=Student.objects.all()
    if form.is_valid():
        form.save()
        return redirect('register_student')
    context={
        'form':StudentCreateForm,
        'queryset':queryset

    }
    return render(request,'register_student.html',context)
def admin_view(request):
    queryset=User.objects.all()
    context={
        'queryset':queryset
    }
    return render(request,'admin.html',context)

def subject_teacher(request):

    return render(request,'subject_teacher.html')
def staff_student(request):
    queryset= Student.objects.count()
    query=Student.objects.filter(sex='Male').count()
    querys=Student.objects.filter(sex='Female').count()
    staff_q1=User.objects.count()
    staff_q2=User.objects.filter(sex='Male').count()
    staff_q3=User.objects.filter(sex='Female').count()
    context={
        'queryset': queryset,
        'query':query,
        'querys':querys,
        'staff_q1':staff_q1,
        'staff_q2':staff_q2,
        'staff_q3':staff_q3,
    }
    return render(request,'staff_student.html',context)
def teacher_view(request):

    queryset=Class.objects.filter(user_id=request.user).values_list('subject__name','name','stream').distinct()
    context={
            'queryset':queryset

        }
    
    return render(request,'teachers_dash.html',context)