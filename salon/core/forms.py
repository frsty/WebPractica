from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1']

class ContactForm(forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'draggable': False}))