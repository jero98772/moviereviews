from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,"home.html",{"name":"Victor Daniel Arango Sohm"}) 

def about(request):
	return render(request,"about.html",{"history":"idk"}) 