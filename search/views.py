from django.shortcuts import render
from django.http import JsonResponse
from utils.utils import getRecommand
import time

# Create your views here.
def search(request):
    result = {"name1":"John","name2":"Mary","name3":"Robert","name4":"James","name5":"Jennifer"}
    if request.method=="POST":
        firstName = request.POST.get('firstName')
        year = request.POST.get('year')
        sex = request.POST.get('sex')
        sex = "male" if sex=="男" else "female"

        # print(firstName, year, sex)
        # print(type(firstName),type(year),type(sex))

        result = {"name1":"Hello","name2":"Got","name3":"One","name4":"Request","name5":"Jennifer"}
        time.sleep(2)

        # recommand = getRecommand(year,sex,firstName)
        # seq = 0
        # for i in result:
        #     result[i] = recommand[seq]
        #     seq+=1

        return JsonResponse(result)
    else:
        return render(request, 'search/search.html',result)