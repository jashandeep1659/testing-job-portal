from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
from job.models import *
from datetime import date
from django.contrib.auth.decorators import user_passes_test, login_required
def home(request):
    students = Student_with_job.objects.all()[:4]
    context = {
        'students':students
    }
    return render(request, 'core/basic/home.html',context)

def latest_jobs(request):
    latest_jobs= Job_Post.objects.filter(breaking_rules=False)
    context={
    'latest_jobs':latest_jobs
    }
    return render(request, 'core/basic/latest_jobs.html', context)

def job_view(request, id , slug):
    post = get_object_or_404(Job_Post, id=id ,slug=slug)
    today = date.today()
    open = False
    if today <= post.end_date and today >= post.start_date:
        open = True
    else:
        open = False

    context = {
    'post':post,
    'open':open,
    }
    return render(request, 'core/basic/job_view.html', context)

@login_required(login_url = 'login')
def apply_job(request, id , slug):
    post= get_object_or_404(Job_Post, id=id ,slug=slug)
    user = request.user
    try:
        already_done =form_of_post.objects.get(post = post , student =user)
        return redirect('job_view', post.id, post.slug)
    except:
        try:
            student_application_data1 = student_application_data.objects.get(student= user)
            alternative_number= student_application_data1.alternative_number
            eduction= student_application_data1.eduction
            age= student_application_data1.age
            finished_in= student_application_data1.finished_in
            finished_in = finished_in.strftime('%Y-%m-%d')
            address= student_application_data1.address
            city= student_application_data1.city
            pin_code= student_application_data1.pin_code
        except:
            pass
        if post.end_date >= date.today() and post.start_date <= date.today() :
            if request.method == 'POST':
                first_name = user.first_name
                last_name = user.last_name
                email = user.email
                phone_number = user.phone_number
                age = request.POST['age']
                eduction = request.POST['eduction']
                finished_in = request.POST['finished_in']
                alternative_number = request.POST['alternative_number']
                address = request.POST['address']
                city = request.POST['city']
                pin_code = request.POST['pin_code']

                if (age) and  (eduction) and  (finished_in) and  (alternative_number) and  (address) and  (city) and  (pin_code):
                    try:
                        student_application_data1 = student_application_data.objects.get(student= user)
                        student_application_data1.alternative_number= alternative_number
                        student_application_data1.age= age
                        student_application_data1.address= address
                        student_application_data1.pin_code= pin_code
                        student_application_data1.finished_in= finished_in
                        student_application_data1.city= city
                        student_application_data1.pin_code= pin_code
                        student_application_data1.eduction= eduction
                        student_application_data1.save()

                        # submiting the real form
                        form = form_of_post.objects.create(teacher = post.by ,student= user,post=post,first_name = user.first_name, last_name=user.last_name,email=user.email,phone_number = user.phone_number,age=student_application_data1.age , eduction= student_application_data1.eduction ,finished_in= student_application_data1.finished_in, alternative_number =student_application_data1.alternative_number,address=student_application_data1.address, city= student_application_data1.city, pin_code= student_application_data1.pin_code )

                        form.save()
                    except:
                        student_application_data1 = student_application_data.objects.create(student=user, finished_in = finished_in,alternative_number= alternative_number,age= age,address =address,city = city,pin_code= pin_code,eduction=eduction)
                        student_application_data1.save()


                        form = form_of_post.objects.create(teacher = post.by ,student= user,post=post,first_name = user.first_name, last_name=user.last_name,email=user.email,phone_number = user.phone_number,age=student_application_data1.age , eduction= student_application_data1.eduction ,finished_in= student_application_data1.finished_in, alternative_number =student_application_data1.alternative_number,address=student_application_data1.address, city= student_application_data1.city, pin_code= student_application_data1.pin_code )

                        form.save()
                else:
                    error  = 'Please Complete form completely'

        else:
            return redirect('job_view', post.id, post.slug)
        context = {
        'post':'post'
        }
        try:
            if alternative_number:
                context['alternative_number']=alternative_number
                context['age']=age
                context['city']=city
                context['pin_code']=pin_code
                context['eduction']=eduction
                context['finished_in']=finished_in
                context['address']=address
        except:
            pass
        return render(request, 'core/basic/apply_job.html',context)

@login_required(login_url = 'login')
def my_applications(request):
    user = request.user
    posts= form_of_post.objects.filter(student = user) 
    context={
        'posts':posts,
    }
    return render(request, 'core/basic/my_applications.html',context)
