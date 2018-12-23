from django import forms


class ApplicantSignIn(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())


class CorporateSignIn(forms.Form):
    co_user_name = forms.CharField(label='user name', max_length=100)
    name = forms.CharField(label="corporate name", max_length=100)
    email = forms.EmailField(label="your email", max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())


class ApplicantLogin(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class CorporateLogin(forms.Form):
    co_user_name = forms.CharField(label='user name', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class CreateAnnouncement(forms.Form):
    corporate_name = forms.CharField(label="corporate name", max_length=100)
    corporate_link = forms.CharField(label="your website")
    job_issue = forms.CharField(label="job issue", max_length=100)
    job_fields = forms.CharField(label="job fields separate fields by #")
    job_salary = forms.IntegerField(label="job salary")
    end_time = forms.IntegerField(label="end time")
    description = forms.TimeField()
