from django.shortcuts import render

# Create your views here.
from members.forms import SignupForm


def signup(request):
    
    form = SignupForm()
    context = {
        'form': form
    }

    return render(request, 'members/signup.html', context)
