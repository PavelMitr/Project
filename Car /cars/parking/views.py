from django.shortcuts import render, redirect

from .models import Parking
from .forms import ParkingForm


def index(request):
    return render(request, 'parking/index.html')

def parking(request):
    parkings = Parking.objects.all()
    return render(request, 'parking/parking.html', context={'parking': parkings})

def parkingq(request, park_id):
    park = Parking.objects.get(id=park_id)
    return render(request, 'parking/parkingq.html', context={'park':park, 'park_id': park_id})

def new_parkin(request):
    if request.method !='POST':
        form = ParkingForm()
    else:
        form = ParkingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('parking:parking')
        
    return render(request, 'parking/new_parkin.html', context={'form': form})

def edit_park(request, pk):
    form = Parking.objects.get(pk=pk)
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parking:parking' )
    else:
        form = ParkingForm(instance=form)
            
    return render (request, 'parking/edit.html', context={'form': form, 'pk': pk})
         

 
def delete(request , par_id):
    par = Parking.objects.get(id=par_id)
    par.delete()
    
    return render (request ,'parking/parking.html' , {'par': par, 'par_id': par_id})












# def parkings(request,parking_id):
#     parkinge = Parking.objects.get(id=parking_id)
#     return render(request ,'parking/parking_id.html', context={'parkingq': parkinge})
