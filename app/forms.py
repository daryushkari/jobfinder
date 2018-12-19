from django import forms


class ApplicantSignIn(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())
    image = forms.FileField(label='your Image', required=False)


class CorporateSignIn(forms.Form):
    co_user_name = forms.CharField(label='user name', max_length=100)
    name = forms.CharField(label="corporate name", max_length=100)
    email = forms.EmailField(label="your email", max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())
    image = forms.FileField(label='your Image', required=False)


