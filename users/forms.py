from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from . import models

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = models.Users
        exclude = ['id']