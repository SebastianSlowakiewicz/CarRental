from django.shortcuts import render
from . import forms

def register(request):
    from_user_register = forms.RegisterUserForm()
    context = {'form_user_register': from_user_register}
    return render(request, 'users/register.html.jinja')

def login(request):
    return render(request, 'users/login.html.jinja')


def logout(request):
    return render(request, 'users/logout.html.jinja')
