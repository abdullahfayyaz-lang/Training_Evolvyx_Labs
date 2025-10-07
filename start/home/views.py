from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={#its used to extract data from models and then pass it to templates
        "variable":"Enemy is on the website"
    }
    return render(request,"index.html",context)
#   return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is aboutpage")

def services(request):
    return HttpResponse("This is servicespage")

def contact(request):
    return HttpResponse("This is contactpage")

