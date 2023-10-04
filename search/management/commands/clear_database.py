from django.core.management.base import BaseCommand
from search.models import NameStore

# collect data from ssa website and write into sqlite database

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        NameStore.objects.all().delete()