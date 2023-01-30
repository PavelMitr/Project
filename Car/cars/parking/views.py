from django.shortcuts import render, redirect

from .models import Parking
from .forms import ParkingForm
# Create your views here.

def index(request):
    
    return render(request, 'parking/index.html')

def parking(request):
    
    parkings = Parking.objects.all()
    
    print(parkings)
    
    
    return render(request, 'parking/parking.html' , context={'parking': parkings})


def new_parkin(request):
    if request.method !='POST':
        form = ParkingForm
    else:
        form = ParkingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('parking:parking')
        
    return render(request, 'parking/new_parkin.html', context={'form':form})















# def parkings(request,parking_id):
#     parkinge = Parking.objects.get(id=parking_id)
#     return render(request ,'parking/parking_id.html', context={'parkingq': parkinge})
