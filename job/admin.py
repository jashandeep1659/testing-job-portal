from django.contrib import admin

# Register your models here.
from .models import *
class Student_with_job_Amdin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name',]}
admin.site.register(Student_with_job ,Student_with_job_Amdin)

# class Job_Post(admin.Mo)
admin.site.register(Job_Post)

class student_application_data_admin(admin.ModelAdmin):
    list_display= ['student',]
admin.site.register(student_application_data,student_application_data_admin)


class form_of_post_admin(admin.ModelAdmin):
    list_display = ['email','first_name','eduction']

admin.site.register(form_of_post,form_of_post_admin)
