from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def homev(request):
    return render(request,"home.html")

def aboutv(request):
    return render(request,"about.html")

def galleryv(request):
    return render(request,"gallery.html")