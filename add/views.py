from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def hello(request):
    return render(request,'add.html')
def add(request):
    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])
    result=val1+val2
    return render(request,"add.html",{'Add_result':result})
def multi(request):
    val1=int(request.GET["num3"])
    val2=int(request.GET["num4"])
    result=val1*val2

    return render(request,"add.html",{'Multi_result':result})

def sub(request):
    val1=int(request.GET["num5"])
    val2=int(request.GET["num6"])
    result=val1-val2

    return render(request,"add.html",{'sub_result':result})

def div(request):
    val1=int(request.GET["num7"])
    val2=int(request.GET["num8"])
    result=val1//val2

    return render(request,"add.html",{'div_result':result})