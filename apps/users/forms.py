from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import*


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'bio', 'job_role', 'verified','cover_photo']
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}),
            'picture': forms.ClearableFileInput(),
            'cover_photo': forms.ClearableFileInput(),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }




class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
