from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant, Corporate
from django.shortcuts import render
from django.http import HttpResponseRedirect
import templates.front
from . import forms
from .models import db
from app import models
# Create your views here.

# home page


def hello(request):
    return render(request, 'front/index.html')

# applicant sign up


def applicant(request):
    if request.method == "POST":
        form = forms.ApplicantSignIn(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if confirm_password != password:
                pass
            x, y = models.applicant_sign_up(first_name, last_name, user_name, password, email)
            return HttpResponse(y)
    else:
        form = forms.ApplicantSignIn(request.POST)

    return render(request, 'front/applicant_templates/applicant_sign_in.html', {'form': form})


def applicant_login(request):
    pass



# corporate sign up


def corporate(request):
    if request.method == "POST":
        form = forms.CorporateSignIn(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['co_user_name']
            email = form.cleaned_data['email']

            return HttpResponse(str(email)+str(first_name))
    else:
        form = forms.CorporateSignIn(request.POST)

    return render(request, 'front/corporate_templates/corporate_sign_in.html', {'form': form})
