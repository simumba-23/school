from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )


    
    class Meta:
        model=User
        fields=['username','password']

class UserRegisterForm(forms.ModelForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    confirm_password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password','confirm_password','role','sex']

        

class ClassCreateForm(forms.ModelForm):
    class Meta:
        model=Class
        fields=['name','stream','subject','user','student']    
class StudentCreateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_Name','middle_Name','last_Name','sex','phone_number']   
class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name','code'] 

class ScoreCreateForm(forms.ModelForm):
    class Meta:
        model=Score
        fields=['marks','rank','student','subject','user']   



