from django.shortcuts import render
from . import forms

def register(request):
    form_users_register = forms.RegisterUserForm()
    context = {'form_users_register': form_users_register}
    return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'users/login.html.jinja')

def logout(request):
    return render(request, 'users/logout.html.jinja')