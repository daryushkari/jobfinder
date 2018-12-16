from django import forms


class ApplicantSignIn(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())
