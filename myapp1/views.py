from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def f1(request):
    return HttpResponse("<h1>This is V1 from myapp1</h1>")

def f2(request):
    return render(request,'home.html')

def view(request):
    return render(request,'staticpage.html')
