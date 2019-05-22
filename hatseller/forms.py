from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.http import request

def validate_password(value):
    if len(value) < 8:
        raise ValidationError(
            _('password must have more than 8 characters'),
        )

class MyLoginForm(forms.Form):
    user = forms.CharField(max_length=100, label='Username:')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password:', required=False)

    def clean_password(self):
        data = self.cleaned_data['password']

        if len(data) == 0:
            raise forms.ValidationError("โปรดกรอก password")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('user')
        password = cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            raise forms.ValidationError('Wrong username or password!')

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )

    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'name': 'first_name'
            }
        ),
        required=False
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'name': 'last_name'
            }
        ),
        required=False
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }
        ),
        required=False,
        validators=[validators.EmailValidator]
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        validators=[validate_password]
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        validators=[validate_password]
    )

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if len(data) == 0:
            raise forms.ValidationError("โปรดกรอกชื่อจริง")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if len(data) == 0:
            raise forms.ValidationError("โปรดกรอกชื่อจริง")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        con_password = cleaned_data.get('confirm_password')

        if password != con_password:
            raise forms.ValidationError('password ไม่เหมือนกัน')
