from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SigninForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Password'
            }
        )
    )


class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Username'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Email'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Confirm password'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
