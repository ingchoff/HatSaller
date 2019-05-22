from django import forms
from django.contrib.auth import authenticate
from django.http import request


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
