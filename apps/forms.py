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

class UserRegisterForm(forms.ModelForm): 
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','password','confirm_password','role','sex']

        

class ClassCreateForm(forms.ModelForm):
    class Meta:
        model=Class
        fields=['name']    
class StudentCreateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['firstName','middleName','lastName','date_Of_Birth','sex','class_stream']   
class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name','code'] 
