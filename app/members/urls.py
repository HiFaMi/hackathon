from django.urls import path
from .views import *

app_name = 'members'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('facebook-login/', facebook_login, name='facebook-login'),
    path('signout/', sign_out, name='sign-out')
]