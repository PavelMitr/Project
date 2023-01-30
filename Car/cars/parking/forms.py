from django import forms
from .models import Parking

class ParkingForm(forms.ModelForm):
    model = Parking
    fields = ['text']
    tex = {'text':''}
