from django.shortcuts import render
from django.http import JsonResponse
from utils.utils import getRecommand

# Create your views here.
def search(request):
    result = {"name1":"aaa","name2":"aaa","name3":"aaa","name4":"aaa","name5":"aaa"}
    if request.method=="POST":
        firstName = request.POST.get('firstName')
        year = request.POST.get('year')
        sex = request.POST.get('sex')
        sex = "male" if sex=="男" else "female"

        print("get POST~~~")
        print(firstName,year,sex)

        recommand = getRecommand(year,sex,firstName)
        seq = 0
        for i in result:
            result[i] = recommand[seq]
            seq+=1

        return JsonResponse(result)
    else:
        return render(request, 'search/search.html',result)