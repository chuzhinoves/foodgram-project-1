from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'username', 'email']