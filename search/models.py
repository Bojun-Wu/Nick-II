from django.db import models

# Create your models here.
# store history search result(save api usage)
class NameStore(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    recommand1 = models.CharField(max_length=50)
    recommand2 = models.CharField(max_length=50)
    recommand3 = models.CharField(max_length=50)
    recommand4 = models.CharField(max_length=50)
    recommand5 = models.CharField(max_length=50)

    def __str__(self):
        return 'name: %s, gender: %c, birth year: %d' %(self.name, self.gender, self.year)