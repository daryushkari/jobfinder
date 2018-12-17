from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant, Corporate
from django.shortcuts import render
from django.http import HttpResponseRedirect
import templates.front
from . import forms

# Create your views here.


def hello(request):
    return render(request, 'front/index.html')


def corporate(request):
    if request.method == "POST":

        form = forms.ApplicantSignIn(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            return HttpResponse(str(email)+str(first_name))
    else:
        form = forms.ApplicantSignIn(request.POST)
        print("get request")
    return render(request, 'front/corporate_templates/corporate_sign_in.html', {'form': form})


def applicant(request):
    if request.method == "POST":

        form = forms.ApplicantSignIn(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            return HttpResponse(str(email)+str(first_name))
    else:
        form = forms.ApplicantSignIn(request.POST)
        print("get request")
    return render(request, 'front/applicant_templates/applicant_sign_in.html', {'form': form})
