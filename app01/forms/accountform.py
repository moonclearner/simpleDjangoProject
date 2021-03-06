from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5)
    password = forms.CharField(min_length=5)
    email = forms.EmailField()
