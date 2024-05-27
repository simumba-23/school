from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=50)
    office_number = models.IntegerField()
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    office = models.ForeignKey(Office,on_delete=models.CASCADE,null=True)
    CHOICES=[
        ('Academic Master','Academic Master'),
        ('School Principal','School Principal'),
        ('Teacher','Teacher'),
        ('School Admin','School Admin'),
        ('Student','Student'),


    ]
    middle_Name = models.CharField(max_length=200) 
    role=models.CharField(max_length=50,choices=CHOICES)
    date_Of_Birth=models.DateField(null=True)    
    CHOICES=[
        ('Male','Male'),
        ('Female','Female')
    ]
    sex=models.CharField(max_length=10,choices=CHOICES)
    
class Class(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class ClassStream(models.Model):
    classes=models.ForeignKey(Class,on_delete=models.CASCADE)
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.classes},{self.stream}'
    
class Student(models.Model):
    SEXCHOICES=[
        ('Male','Male'),
        ('Female','Female') ]
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    classes = models.ForeignKey(Class,on_delete=models.CASCADE,null=True)
    

    
    def __str__(self):
        return self.middle_name

class Subject(models.Model):
    name=models.CharField(max_length=100 )
    code=models.CharField(max_length=100 )
    
    def __str__(self):
        return self.name

class Score(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='Score')
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    marks=models.CharField(max_length=200)
    grade=models.CharField(max_length=200)
    
    def __str__(self):
        return self.marks
class TeacherSubject(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    classes_Stream= models.ForeignKey(ClassStream,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user},{self.subject},{self.classes_Stream}'
    
class Permission(models.Model):
    statusChoice=[
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Denied','Denied'),

        ]
    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=statusChoice,default='pending')

    def __str__(self):
        return self.title



