from django.contrib import admin
from .models import Driver, Car, StateNumber, Parking

# Register your models here.
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Parking)
admin.site.register(StateNumber)