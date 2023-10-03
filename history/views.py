from django.shortcuts import render
from .models import BabyName
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# Create your views here.
def boy(request):
    data = BabyName.objects.filter(year = 2010).filter(gender="M").order_by('rank')
    context = {'data':data}
    if request.method=="POST":
        year = int(request.POST.get('decade'))
        data = BabyName.objects.filter(year = year).filter(gender="M").order_by('rank')
        data_json = serializers.serialize('json',data)
        return HttpResponse(data_json,content_type='application/json')

    else:
        return render(request,'history/boypage.html',context)

def girl(request):
    data = BabyName.objects.filter(year = 2010).filter(gender="F").order_by('rank')
    context = {'data':data}
    if request.method=="POST":
        year = int(request.POST.get('decade'))
        data = BabyName.objects.filter(year = year).filter(gender="F").order_by('rank')
        data_json = serializers.serialize('json',data)
        return HttpResponse(data_json,content_type='application/json')

    else:
        return render(request,'history/girlpage.html',context)

# def girl(request):
#     data = BabyName.objects.filter(year = 2010).filter(gender="F").order_by('rank')
#     context = {'data':data}
#     if request.method=="POST":
#         year = int(request.POST.get('decade'))
#         # print("got POST",year)
#         data = BabyName.objects.filter(year = year).filter(gender="F").order_by('rank')
#         # data = {1:{'name':'Matthew','year':1990,'number':'351,649'}}
#         # print(type(data))
#         data = list(data)
#         output = {}
#         print(len(data))
#         for i in range(len(data)):
#             output[i] = {}
#             output[i]['name']=data[i].name
#             output[i]['people']=data[i].people
#         return JsonResponse(output)

#     else:
#         return render(request,'history/girlpage.html',context)