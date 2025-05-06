from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from . import models

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = models.Users
        exclude = ['id']
        fields = ['username', 'email', 'password1', 'password2','first_name', 'last_name', 'phone', 'birth_date', 'identity_document_type', 'identity_document_no']