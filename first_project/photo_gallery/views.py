from django.shortcuts import render
from django.http import HttpResponse

def galleryHomeView(request):
    return HttpResponse("Welcome to the Gallery")