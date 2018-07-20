from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

<<<<<<< HEAD:app/members/views.py
# Create your views here.
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('category')

    form = SignupForm()
    context = {
        'form': form
    }

    return render(request, 'members/signup.html', context)
=======
from ..forms import LoginForm
>>>>>>> origin/dev:app/members/views/login.py

__all__ = (
    'user_login',
)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('category')
            else:
                return HttpResponse("Failed login")
    form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'members/login.html', context)
