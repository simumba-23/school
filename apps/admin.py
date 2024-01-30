from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Score)
admin.site.register(Class)
admin.site.register(ClassStream)
admin.site.register(StudentSubjectScore)
admin.site.register(Stream)

