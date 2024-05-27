from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','password']

        widgets = {
                'username':forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'placeholder':'Enter Username',

                    }
                ),
                'password':forms.PasswordInput(
                    attrs={
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'placeholder':' Enter Password'
                    
                    }
                )
        }
class studentLoginForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','password']

        widgets = {
                'username':forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'placeholder':'Enter Username'

                    }
                ),
                'password':forms.PasswordInput(
                    attrs={
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'placeholder':' Enter Password'
                    
                    }
                )
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm): 
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','middle_Name','password','office','role','sex','date_Of_Birth']
        widgets = {
                'date_Of_Birth':forms.DateTimeInput(
                    attrs = {
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'type':'date'

                    }
                ),
                
        }

        
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name','last_name', 'email', 'date_Of_Birth', 'sex']
        widgets = {
                'date_Of_Birth':forms.DateTimeInput(
                    attrs = {
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'type':'date'

                    }
                ),
                
        }
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model =CustomUser
        fields = ['username', 'first_name','last_name', 'email', 'date_Of_Birth', 'sex']
        widgets = {
                'date_Of_Birth':forms.DateTimeInput(
                    attrs = {
                        'class': 'form-control',
                        'style':'max-width: 400px;',
                        'type':'date'

                    }
                ),
                
        }

class ClassCreateForm(forms.ModelForm):
    class Meta:
        model=Class
        fields=['name']    
class StudentCreateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['classes']  
        
class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name','code'] 

class SubjectTeacherForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=CustomUser.objects.filter(role='Teacher'))
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    classes_Stream = forms.ModelChoiceField(queryset=ClassStream.objects.all())

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(SubjectTeacherForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['teacher'].initial = self.instance.user
            self.fields['subject'].initial = self.instance.subject
            self.fields['classes_Stream'].initial = self.instance.classes_Stream

    def save(self):
        # Extract cleaned data from the form
        teacher = self.cleaned_data['teacher']
        subject = self.cleaned_data['subject']
        classes_Stream = self.cleaned_data['classes_Stream']

        if self.instance:
            # Update the existing instance
            self.instance.user = teacher
            self.instance.subject = subject
            self.instance.classes_Stream = classes_Stream
            self.instance.save()
            return self.instance
        else:
            # Create a new instance
            subject_teacher = TeacherSubject.objects.create(
                teacher=teacher,
                subject=subject,
                classes_Stream=classes_Stream
            )
            return subject_teacher
class ScoreUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')
    # class Meta:
    #     model=TeacherSubject
    #     fields=['user','subject','darasa']
class ModifyRoleForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role']
    
class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['title','description','status']