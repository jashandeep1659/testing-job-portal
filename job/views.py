from django.shortcuts import render, get_object_or_404, redirect

from .models import *
import os
from django.template.defaultfilters import slugify
# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa


from django.contrib.auth.decorators import user_passes_test, login_required
def teacher_check(user):
    return user.is_staff and user.user_role == 'Teacher'

@login_required(login_url = 'login')
@user_passes_test(teacher_check, login_url='login')
def create_post(request):
    user= request.user
    if request.method == "POST":
        title = request.POST['title']
        company_name = request.POST['company_name']
        location = request.POST['location']
        starting_date = request.POST['starting_date']
        end_date = request.POST['end_date']
        starting_salary = request.POST['starting_salary']
        eductaion_required = request.POST['eductaion_required']
        vacancies = request.POST['vacancies']
        image = request.POST['image']
        part_or_full_time = request.POST['part_or_full_time']
        office_or_home = request.POST['office_or_home']
        skills = request.POST['skills']
        if  (title)and (company_name)and (location)and (starting_date)and (end_date)and (starting_salary) and (eductaion_required)and (vacancies)and (image)and (part_or_full_time)and (office_or_home)and (skills):
            post = Job_Post.objects.create(by= user,title = title, company_name = company_name, location = location, start_date = starting_date, end_date = end_date, starting_salary = starting_salary, education_needed = eductaion_required, vacancies = vacancies, image = image, part_or_full_time = part_or_full_time, office_or_home = office_or_home, skills = skills,)
            post.save()
            post.slug = slugify(post.title)
            post.save()

    return render(request, 'job/create_post.html')


def posts_by_teacher(request):
    posts = Job_Post.objects.filter(by =request.user )
    context ={
    'posts':posts
    }
    return render(request,'job/teacher/posts_by_teacher.html',context)

def students_apply(request, id ,slug):
    post = get_object_or_404(Job_Post, id=id , slug=slug)
    if post.by == request.user:
        students = form_of_post.objects.filter(teacher = request.user , post=post)
        context={
        'students':students,
        'post':post
        }
        return render(request,'job/teacher/students_apply.html',context)
    else:
        return redirect('job_view', post.id, post.slug)



def generate_pdf_through_template(request,id ,post_id):
    post = Job_Post.objects.get(id = post_id)
    student = form_of_post.objects.get(id = id )
    student1 = User.objects.get(email = student )
    photo_url = student1.photo.url
    photo_url = 'http://192.168.43.38:8000'+photo_url
    path = "job/teacher/student_form_pdf.html"
    context ={
    'post':post,
    'photo_url':photo_url,
    'student':student,
    }

    html = render_to_string('job/teacher/student_form_pdf.html',context)
    io_bytes = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)

    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)
# /https://stackoverflow.com/questions/59418435/django-html-css-render-to-pdf
