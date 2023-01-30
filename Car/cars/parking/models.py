from django.db import models

# Create your models here.

class Driver(models.Model):
    name =models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class StateNumber(models.Model):
    number = models.TextField(max_length=10)
    
class Car(models.Model):
    model = models.CharField(max_length=20)
    driver_car = models.ForeignKey(Driver, verbose_name=("Водитель машины"), on_delete=models.CASCADE) 
    number_car = models.TextField()
    color = models.TextField()
    
    def __str__(self) :
        return self.model

class Parking(models.Model):
    car = models.ForeignKey(Car, verbose_name=("Модель авто"), on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, verbose_name=("Собственик"), on_delete=models.CASCADE)
    free_place = models.PositiveIntegerField()
    time_start = models.DateTimeField(auto_now_add = True)
    time_stop =  models.DateTimeField(auto_now_add = True) 
    
    
    # def __str__(self):
    #     return self.id

# class Pizza(models.Model):
#     name = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
        
#         return self.text

# class Topping(models.Model):
       
#     pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
#     name= models.TextField()
#     date_added = models.DateTimeField(auto_now_add = True)
    