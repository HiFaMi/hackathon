from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from ..forms import LoginForm

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
                return redirect('login')
            else:
                return HttpResponse("Failed login")
    form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'members/login.html', context)
