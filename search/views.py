from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def search(request):
    result = {"name1":"aaa","name2":"aaa","name3":"aaa","name4":"aaa","name5":"aaa"}
    if request.method=="POST":
        firstName = request.POST.get('firstName')
        year = request.POST.get('year')
        sex = request.POST.get('sex')
        print("get POST~~~")
        print(firstName,year,sex)
        result["name1"] = "bbb"
        return JsonResponse(result)
    else:
        return render(request, 'search/search.html',result)