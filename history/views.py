from django.shortcuts import render

# Create your views here.
def boy(request):
    context = {}
    return render(request,'history/boypage.html',context)

def girl(request):
    context = {}
    return render(request,'history/girlpage.html',context)