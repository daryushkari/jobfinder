from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('corporate/', views.corporate, name='corporate'),
    path('applicant/', views.applicant, name='applicant'),
    path('applicant/login', views.applicant_login, name='applicant/login'),
    path('mainapp/<user_name>', views.mainapp, name="asdf"),
]
