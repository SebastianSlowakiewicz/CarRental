from django.shortcuts import redirect, render
from . import forms
from .forms import RegisterUserForm

def register(request):
    if request.method == 'POST':
        form_user_register = RegisterUserForm(request.POST)
        if form_user_register.is_valid():
            form_user_register.save()
            return redirect('login')
    else:
        form_user_register = RegisterUserForm()

    context = {'form_user_register': form_user_register}
    return render(request, 'users/register.html.jinja', context)

def login(request):
    return render(request, 'users/login.html.jinja')

def logout(request):
    return render(request, 'users/logout.html.jinja')