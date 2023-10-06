from django.core.management.base import BaseCommand
from history.models import BabyName
import requests
from bs4 import BeautifulSoup

# collect data from ssa website and write into sqlite database

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for i in range(1880,2020,10):
            response = requests.get(f"https://www.ssa.gov/oact/babynames/decades/names{i}s.html")
            soup = BeautifulSoup(response.text,"html.parser")
            temp = 0
            rank, name, ppl = 0, '', ''
            for j in soup.find_all("td")[1:-2]:
                data = j.getText()
                if temp%5==0:
                    rank = int(data)
                elif temp%5==1:
                    name = data
                elif temp%5==2:
                    ppl = data
                    BabyName.objects.create(rank = rank, gender = 'M', name=name, people = ppl, year = i)
                elif temp%5==3:
                    name = data
                elif temp%5==4:
                    ppl = data
                    BabyName.objects.create(rank = rank, gender = 'F', name=name, people = ppl, year = i)
                temp+=1