from django.shortcuts import render
from user.models import *
# Create your views here.
from django.contrib.auth.decorators import user_passes_test, login_required
def superuser_check(user):
    return user.is_superuser

@login_required(login_url = 'login')
@user_passes_test(superuser_check, login_url='login')
def teacher_controls(request):
    stu_teachers = User.objects.filter(request_as_teacher= True, user_role = 'Student')
    if request.method =='POST':
        do = request.POST['do']
        email = request.POST['email']
        if do == 'accept':
            user = User.objects.get(email= email)
            user.is_staff = True
            user.user_role = "Teacher"
            user.request_as_teacher = False
            user.save()
        elif do=='reject':
            user = User.objects.get(email= email)
            user.is_staff  = False
            user.rejected_once = True
            user.user_role = 'Student'
            user.request_as_teacher = False
            user.save()
    context= {
    'stu_teachers':stu_teachers,
    }
    return render(request,'admin_controls/controls/teacher-controls.html', context)


def all_users(request):
    users = User.objects.all()
    context = {
    'users':users
    }
    return render(request, 'admin_controls/controls/all_users.html',context)
