from django.shortcuts import render
from .models import BabyName

# Create your views here.
def boy(request):
    context = {}
    return render(request,'history/boypage.html',context)

def girl(request):
    context = {}
    return render(request,'history/girlpage.html',context)