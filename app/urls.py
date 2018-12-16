from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('corporate/', views.corporate, name='corporate'),
    path('applicant/', views.applicant, name='applicant'),
    #path('sin/', views.get_name, name='sign_in')
]
