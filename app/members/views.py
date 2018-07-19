from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from members.forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("you're signup successfully")

    form = SignupForm()
    context = {
        'form': form
    }

    return render(request, 'members/signup.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('login')
            else:
                return HttpResponse("Failed login")
    form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'members/login.html', context)
