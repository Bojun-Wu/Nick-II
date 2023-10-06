from django.shortcuts import render
from django.http import JsonResponse
from utils.utils import getRecommand,transName
from .models import NameStore
import time
from .forms import NameStoreForm

def search(request):
    result = {"name1":"John","name2":"Mary","name3":"Robert","name4":"James","name5":"Jennifer"}

    if request.method=="POST":
        form = NameStoreForm(request.POST)
        # result = {"name1":"Hello","name2":"Got","name3":"One","name4":"Request","name5":"Jennifer"}

        # check form validation
        if form.is_valid():
            data = form.cleaned_data
            name = data["firstName"]
            nameTrans = transName(name)
            sex="M" if data["sex"]=="男" else "F"

            try:
                # print(nameTrans,data["year"],sex)
                recommand = NameStore.objects.get(name=nameTrans,year=data["year"],gender=sex)

                result["name1"] = recommand.recommand1
                result["name2"] = recommand.recommand2
                result["name3"] = recommand.recommand3
                result["name4"] = recommand.recommand4
                result["name5"] = recommand.recommand5
                print(f"{nameTrans}, {name} from database")
            
            except Exception as e:
                sexShort = "male" if sex=="M" else "female"
                
                print(e,"get data from openai data",data["year"],sexShort,name)
                recommand = getRecommand(data["year"],sexShort,name)

                # store retrieved data to database
                NameStore.objects.create(name=nameTrans, gender=sex, year=data["year"], recommand1=recommand[0],recommand2=recommand[1],recommand3=recommand[2],recommand4=recommand[3],recommand5=recommand[4])

                seq = 0
                for i in result:
                    result[i] = recommand[seq]
                    seq+=1
                print(f"{nameTrans}, {name} from openai")

        else:
            print("Error ", form.errors.keys())
            result["error"]=form.errors

        return JsonResponse(result)
    
    else:
        return render(request, 'search/search.html',result)