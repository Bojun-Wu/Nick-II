from django import forms
from .validators import validate_name

class NameStoreForm(forms.Form):
    GENDER_CHOICES = (
        ('男', 'Male'),
        ('女', 'Female'),
    )
    firstName = forms.CharField(max_length=50,validators=[validate_name],required=True)
    lastName = forms.CharField(max_length=50,validators=[validate_name],required=True)
    year = forms.IntegerField(max_value=2010, min_value=1880, step_size=1,required=True, error_messages={"required":"必要欄位"})
    sex = forms.ChoiceField(choices = GENDER_CHOICES)