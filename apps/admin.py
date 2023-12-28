from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Score)
admin.site.register(Class)

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name','stream','subject','teachedby']