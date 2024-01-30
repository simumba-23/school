from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES=[
        ('Academic Master','Academic Master'),
        ('School Principal','School Principal'),
        ('Teacher','Teacher'),
        ('School Admin','School Admin'),

    ]
    role=models.CharField(max_length=50,choices=CHOICES)
    
    CHOICES=[
        ('Male','Male'),
        ('Female','Female')
    ]
    sex=models.CharField(max_length=10,choices=CHOICES)
    confirm_password = models.CharField(max_length=50)

class Class(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class ClassStream(models.Model):
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)
    darasa=models.ForeignKey(Class,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.stream},{self.darasa}'
    
class Student(models.Model):
    SEXCHOICES=[
        ('Male','Male'),
        ('Female','Female')    ]
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200) 
    lastName = models.CharField(max_length=200)
    date_Of_Birth=models.DateField()
    sex=models.CharField(max_length=20,choices=SEXCHOICES)
    class_stream = models.ForeignKey(ClassStream,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.firstName

class Subject(models.Model):
    name=models.CharField(max_length=100 )
    code=models.CharField(max_length=100 )
    
    def __str__(self):
        return self.name
    
class Score(models.Model):
    marks=models.CharField(max_length=200)
    grade=models.CharField(max_length=200)
    
    def _str_(self):
        return self.marks

class StudentSubjectScore(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    score = models.ForeignKey(Score,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student

