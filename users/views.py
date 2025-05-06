from django.shortcuts import render
from . import forms

def register(request):
    if request.method == 'post':
        form_users_register = forms.RegisterUserForm(request.POST)
        if form_users_register.is_valid():
            form_users_register.save()
            context = {'form_users_register': form_users_register}
            return render(request, 'users/register.html.jinja', context=context)
    else:
        context = {'message': 'Zonk!'}
    return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'users/login.html.jinja')

def logout(request):
    return render(request, 'users/logout.html.jinja')