from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Content, Card


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    dict_mob = {
        'mob': Content.objects.all()
    }

    return render(request, 'about.html', dict_mob)


def product(request):
    dict_card = {
        'card': Card.objects.all()
    }
    return render(request, 'product.html', dict_card)


def file(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pswd']

        username = User.objects.get(email=email.lower()).username

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return HttpResponse("Successfully Login")
        else:
            return HttpResponse("Invalid login")

    return render(request, 'file.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']

        if pass1 != pass2:
            return HttpResponse("Yr password is incorrect")

        else:
            myuser = User.objects.create_user(username=uname, email=email, password=pass1)
            myuser.save()
            return redirect('file')
    return render(request, 'signup.html')
