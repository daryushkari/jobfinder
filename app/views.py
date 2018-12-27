from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant, Corporate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import templates.front
from . import forms
from .models import db
from .utilities.create_validation_code import send_validation_code
from app import models
import secrets
# Create your views here.
from .model_functions.applicant_login import send_token


# home page


def hello(request):
    return render(request, 'main/index.html')

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
            validation_code = send_validation_code(email)
            token = str(secrets.token_hex())
            x, y = models.applicant_sign_up(first_name, last_name, user_name, password, email, token, validation_code)
            if x:
                return HttpResponseRedirect('/applicant/login')
            else:
                return HttpResponse(y)
    else:
        form = forms.ApplicantSignIn(request.POST)

    return render(request, 'front/applicant_templates/applicant_sign_in.html', {'form': form})


def applicant_login(request):
    if request.method == "POST":
        form = forms.ApplicantLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            x, token = send_token(username, password)
            if x:
                token = '/mainapp/'+token
                return HttpResponseRedirect(token)
            elif token == "user not valid":
                return HttpResponse("user not valid")
            return HttpResponse("username or password is wrong")
    form = forms.ApplicantLogin(request.POST)
    return render(request, 'front/applicant_templates/applicant_login.html', {'form': form})


# corporate sign up

def mainapp(request, user_name):
    return HttpResponse(str(user_name))

def corporate(request):
    if request.method == "POST":
        form = forms.CorporateSignIn(request.POST)
        if form.is_valid():
            co_user_name = form.cleaned_data['co_user_name']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if confirm_password != password:
                pass
            validation_code = send_validation_code(email)
            token = str(secrets.token_hex())
            x, y = models.corporate_sign_up(co_user_name, name, email, description, password, token, validation_code)
            return HttpResponse(y)
    else:
        form = forms.CorporateSignIn(request.POST)

    return render(request, 'front/corporate_templates/corporate_sign_in.html', {'form': form})
