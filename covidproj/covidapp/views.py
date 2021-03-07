from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
# result = requests.get('​https://api.rootnet.in/covid19-in/contacts/')
# print(result)
def index(request):
    url = "https://api.rootnet.in/covid19-in/hospitals/beds"
    urln = url.replace('\u200b', '')
    result = requests.get(urln)
    data = result.json()
    return render(request, 'index.html',{'data':data})

def homepage(request):
    return render(request, 'base.html')

def about(request):
    url = "​https://api.rootnet.in/covid19-in/contacts/"
    urln = url.replace('\u200b', '')
    result = requests.get(urln)
    data = result.json()
    return render(request, 'helpline.html',{'data':data})


def notify(request):
     url = "​https://api.rootnet.in/covid19-in/notifications/"
     urln = url.replace('\u200b', '')
     result = requests.get(urln)
     data = result.json()
     return render(request, 'notifications.html',{'result':data})


def medical_colleges(request):
     url = "​​https://api.rootnet.in/covid19-in/hospitals/medical-colleges"
     urln = url.replace('\u200b', '')
     result = requests.get(urln)
     data = result.json()
     return render(request, 'colleges.html',{'result':data})


def comparison(request):
     url1 = "https://api.rootnet.in/covid19-in/stats/history"
     url2 = "https://api.rootnet.in/covid19-in/stats/testing/history"
     urln1 = url1.replace('\u200b', '')
     urln2 = url2.replace('\u200b', '')
     result1 = requests.get(urln1)
     result2 = requests.get(urln2)
     data1 = result1.json()
     data2 = result2.json()
     return render(request, 'comparison.html',{'data1':data1, 'data2':data2})

