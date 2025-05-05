from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class ConnexionForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'nom user', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'mdp', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
