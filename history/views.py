from django.shortcuts import render
from .models import BabyName
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.management import call_command

# Create your views here.
def history(request, gender):
    if not BabyName.objects.all():
        print("database is empty, collect data from SSA")
        call_command("collectSSA")

    sex = "M" if gender=="boy" else "F"
    data = BabyName.objects.filter(year = 2010).filter(gender=sex).order_by('rank')
    context = {'gender':gender, 'data':data}

    if request.method=="POST":
        year = int(request.POST.get('decade'))
        data = BabyName.objects.filter(year = year).filter(gender=sex).order_by('rank')
        data_json = serializers.serialize('json',data)
        return HttpResponse(data_json,content_type='application/json')

    else:
        return render(request,'history/history.html',context)