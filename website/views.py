from django.shortcuts import render
from django.http import HttpResponse
from . import utilitiez
# Create your views here.
# this is gets the request actualy

def home(request):
    return render(request,'home.html',{})

def get_productAsin(request):
         sellerids=5
         return render(request,'home.html',{'sellerid':sellerids} )

def counter(request):
       context={
              'age':"",
              'productLocation':"who is this",
       }
       selleridF=request.POST['sellerid']
       who="asdasd"
       return render(request,'counter.html',{'who':who})