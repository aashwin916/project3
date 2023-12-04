from django.http import HttpResponse
from django.shortcuts import render
from.models import Coffee
# Create your views here.
def demo(request):
    drink=Coffee.object.all()

    return render(request,"index.html",{'result':drink})
# def addition(request):
#     x=int(request.GET['num1'])
#     y= int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})
