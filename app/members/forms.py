

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'authority',
        )


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class UserFoodForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'order'
        ]
