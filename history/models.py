from django.db import models

# Create your models here.
class BabyName(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    name = models.CharField(max_length=200)
    people = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()