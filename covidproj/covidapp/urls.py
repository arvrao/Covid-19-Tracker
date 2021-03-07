from django.urls import path
from . import views
app_name = 'covidapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('advisories/', views.index, name='advisories'),
    path('helpline/', views.about, name='helpline'),
    path('notify/', views.notify, name='notify'),
    path('comparison/', views.comparison, name='comparison'),
    path('medical-colleges/', views.medical_colleges, name='medical_colleges'),
]
