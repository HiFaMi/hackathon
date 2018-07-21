from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..forms import SignupForm

__all__ = (
    'signup',
)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('index')

    form = SignupForm()
    context = {
        'form': form
    }

    return render(request, 'members/signup.html', context)
