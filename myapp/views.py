
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def date_time(request):
    dt=datetime.datetime.now()
    #return HttpResponse("<h1>Current System data and time is :"+str(dt)+"</h1>")
    return render(request, "datetime.html",{'dt':dt})

def v2(request):
    result={'v2':v2,'name': 'abhi'}
    return render(request,"home.html",context=result)

def home(request):
    return render(request, "index12.html")

def math(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    res = a+b
    age = 45
    salary = 5000
    data = {'res':res, 'age':age, 'salary':salary}
    return render(request, 'result.html', context={'data':data})


