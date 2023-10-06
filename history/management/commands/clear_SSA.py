from django.core.management.base import BaseCommand
from history.models import BabyName

# collect data from ssa website and write into sqlite database

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        BabyName.objects.all().delete()