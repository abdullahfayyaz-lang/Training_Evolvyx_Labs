from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is aboutpage")

def services(request):
    return HttpResponse("This is servicespage")

def contact(request):
    return HttpResponse("This is contactpage")

