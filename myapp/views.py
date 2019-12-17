from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Httpresponse</h1>")

def generic(request):
    d={'data':"Babu"}
    return render(request,'generic.html',context=d)

def specific(request):
    fruits={'fruits_name':['Mango','Bannana','Grapes','Dragon_fruit']}
    return render(request,'specific.html',context=fruits)