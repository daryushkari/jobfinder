from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant, Corporate
from django.shortcuts import render
from django.http import HttpResponseRedirect
import templates.front
from . import forms
from .models import db
# Create your views here.


def hello(request):
    return render(request, 'front/index.html')


def applicant(request):
    print("fuck you")
    if request.method == "POST":
        form = forms.ApplicantSignIn(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            return HttpResponse(str(email)+str(first_name))
    else:
        form = forms.ApplicantSignIn(request.POST)

    return render(request, 'front/applicant_templates/applicant_sign_in.html', {'form': form})


def corporate(request):
    print("chuck you")
    if request.method == "POST":
        form = forms.CorporateSignIn(request.POST)
        if form.is_valid():
            print('z')
            first_name = form.cleaned_data['co_user_name']
            email = form.cleaned_data['email']

            return HttpResponse(str(email)+str(first_name))
    else:
        form = forms.CorporateSignIn(request.POST)
    return render(request, 'front/corporate_templates/corporate_sign_in.html', {'form': form})
