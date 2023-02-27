from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationsForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]
        
class LoginForm(UserCreationForm):
# class LoginForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder':'Enter password',
    #     'class':'form-control'
    # }))
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder':'Enter Username',
    #     'class':'form-control'
    # }))

    class Meta:
        model = User
        fields = ['username', 'password']
               