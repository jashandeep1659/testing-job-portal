from django.shortcuts import render , redirect

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def signup(request):
    form = User_creation()
    if request.method == 'POST':
        form = User_creation(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save()
            auth.login(request,user)
            return redirect('home')
    else:
        form = User_creation()
    context = {
    'form':form
    }
    return render(request, 'user/signup.html',context)

def login(request):
    error = None
    if request.method == "POST":
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = auth.authenticate(email= email , password  = password)
        print(password, email)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            error = 'Please check your email and password'
            return render(request, 'user/login.html',{'error':error})


    return render(request, 'user/login.html')

@login_required(login_url = 'login')
def create_teacher(request):
    user = request.user
    if user.rejected_once == False and user.user_role == 'Student':
        if request.method == 'POST':
            graduation = request.POST['graduation']
            image =  request.FILES.get("image",None)
            if (graduation)is not '' and (image) is not None:
                user.qualification = graduation
                user.photo = image
                user.request_as_teacher = True
                user.save()
                return redirect('home')
            else:
                return redirect('home')
    else:
        return redirect('home')
    return render(request, 'user/teacher.html')
