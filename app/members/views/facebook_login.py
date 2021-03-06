import requests
from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect

User = get_user_model()

__all__ = (
    'facebook_login',
)


def facebook_login(request):
    code = request.GET.get('code')
    user = authenticate(request, code=code)

    if user is not None:
        login(request, user)
        return redirect('index')
    return redirect('members:login')