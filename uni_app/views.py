from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
# from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')

def apply_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')

        # print(username, password)

        user = authenticate(request, username=username, password=password) or \
            authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('/apply')
    
    return render(request, 'apply_login.html')

def apply_signup(request):
    if request.method=="POST":
        # full_name =request.POST.get('full_name')
        uname =request.POST.get('username')
        email =request.POST.get('email')
        pass1 =request.POST.get('password')
        pass2 =request.POST.get('repassword')


        if pass1 != pass2:
            messages.error(request, 'password not match!!')
            return redirect('/signup/')

        else:
            if User.objects.filter(username=uname, email=email).exists():
                messages.error(request, 'This Username and Email exists')
                return redirect('/signup/')

            elif User.objects.filter(username=uname).exists():
                messages.error(request, 'This Username already exists')
                return redirect('/signup/')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This Email already exists')
                return redirect('/signup/')
            else:
                my_user = User.objects.create_user( username=uname, email=email, password=pass1)
            # my_user = User.objects.create_user(name=full_name, username=uname, email=email, password=pass1)
            # my_user = CustomUser.objects.create_user(name=full_name, username=uname, email=email, password=pass1)

                my_user.save()
                return redirect('/apply/')
            # return HttpResponse("user save")
    
        # lname =request.POST.get('lastname')
        # city =request.POST.get('city')
        # dob =request.POST.get('dob')
        # my_user= User.objects.create_user(uname, fullname, lname, city, email, dob, pass1)
        # print(uname, fname, lname, city)


    return render(request, 'apply_signup.html')

def about_page(request):
    return render(request, 'about_page.html')

@login_required(login_url='home')
def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')


def logoutpage(request):
    logout(request)
    # return redirect('/apply/')
    return redirect('/')