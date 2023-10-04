from django.shortcuts import render
from django.http import JsonResponse
from utils.utils import getRecommand,transName
from .models import NameStore
import time

# Create your views here.
def search(request):
    result = {"name1":"John","name2":"Mary","name3":"Robert","name4":"James","name5":"Jennifer"}
    if request.method=="POST":
        firstName = request.POST.get('firstName')
        year = request.POST.get('year')
        sex = request.POST.get('sex')
        sex = "M" if sex=="男" else "F"

        # print(firstName, year, sex)
        # print(type(firstName),type(year),type(sex))
        # result = {"name1":"Hello","name2":"Got","name3":"One","name4":"Request","name5":"Jennifer"}
        # time.sleep(2)

        try:
            recommand = NameStore.objects.get(name=transName(firstName),year=int(year),gender=sex)
            result["name1"] = recommand.recommand1
            result["name2"] = recommand.recommand2
            result["name3"] = recommand.recommand3
            result["name4"] = recommand.recommand4
            result["name5"] = recommand.recommand5
            print(f"{transName(firstName)} from database")

        except:
            sex = "male" if sex=="M" else "female"
            recommand = getRecommand(year,sex,firstName)

            # store retrieved data to database
            sex = "M" if sex=="male" else "F"
            NameStore.objects.create(name=transName(firstName), gender=sex, year=int(year), recommand1=recommand[0],recommand2=recommand[1],recommand3=recommand[2],recommand4=recommand[3],recommand5=recommand[4])

            seq = 0
            for i in result:
                result[i] = recommand[seq]
                seq+=1
            print(f"{transName(firstName)} from openai")

        return JsonResponse(result)
    else:
        return render(request, 'search/search.html',result)