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
            return redirect('index')

    form = SignupForm()
    context = {
        'form': form
    }

    return render(request, 'members/signup.html', context)
