from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Activation, MyUser

from django.forms import ValidationError


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(('You can not use this email address.'))
        return email


class LoginForm(forms.Form):
    user_cache = None
    username = forms.CharField(label=('Имя'), widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Имя',
        }))
    password = forms.CharField(
        label=('Пароль'), strip=False, widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Введите пароль',
            }))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(('You entered an invalid username.'))
        if not user.is_active:
            raise ValidationError(('This account is not confirmed.'))

        self.user_cache = user

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
             raise ValidationError(('You entered an invalid password.'))

        return password


class UserForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('name', 'email')