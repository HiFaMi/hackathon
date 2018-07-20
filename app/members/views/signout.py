from django.contrib.auth import logout
from django.shortcuts import redirect


def sign_out(request):
    # if request.method == 'POST'
    logout(request)
    return redirect('index')
        # return()
