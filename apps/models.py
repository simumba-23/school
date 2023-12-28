from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLECHOICES=[
        ('Teacher','Teacher'),
        ('Cleaner','Cleaner'),
        ('Security Officer','Security Officer'),
        ('Labaratory Technician','Labaratory Technician'),
        ('Academic Teacher','Academic Teacher'),
        
        
    ]

    
    role=models.CharField(max_length=100,choices=ROLECHOICES,default='Teacher')
    
    
    CHOICES=[
        ('Male','Male'),
        ('Female','Female')

    ]

    sex=models.CharField(max_length=10,choices=CHOICES, default='Male')
class Student(models.Model):
    SEXCHOICES=[
        ('Male','Male'),
        ('Female','Female')

    ]
    first_Name = models.CharField(max_length=200)
    middle_Name = models.CharField(max_length=200) 
    last_Name = models.CharField(max_length=200)
    sex = models.CharField(max_length=20,choices=SEXCHOICES,default='Male')
    phone_number=models.IntegerField(default='0678190323')
    
    def __str__(self):
        return f'{self.first_Name} {self.middle_Name} {self.last_Name}'
    class Meta:
        db_table= 'Student'

class Subject(models.Model):
    name=models.CharField(max_length=100 )
    code=models.CharField(max_length=100 )
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table= 'Subject'


class Score(models.Model):
    marks=models.CharField(max_length=200)
    rank=models.CharField(max_length=200)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    
    def _str_(self):
        return f'{self.subject}-{self.student}-{self.user}'
    class Meta:
        db_table='Score'

class Class(models.Model):
    name=models.CharField(max_length=100)
    stream=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=2)
    
    def _str_(self):
        return self.name
    
    class Meta:
        db_table='Class'




