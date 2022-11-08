from django.db import models
from django.contrib.auth.models import User
import uuid as uuid_lib
from datetime import datetime

# Create your models here.

#creating a user
class students(models.Model):
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20, null=False, default="")
    rollno = models.IntegerField(null=False, default="")
    mobile = models.CharField(max_length=10, default="")
    username = models.CharField(max_length=20, null=False, default="", unique=True)
    password = models.CharField(max_length=20, null=False, default="")

    def __str__(self):
        return str(self.rollno)+" "+self.name+" "+self.lname

    class Meta:
        verbose_name_plural = "students"
        verbose_name = "student"

#creating a customer
class Mess(models.Model):
    customer = models.ForeignKey(students, default=None, on_delete=models.CASCADE)
    dateOfRegistration = models.DateField(auto_now=False)
    noOfCoupons = models.IntegerField(default=55)
    dateOfExpiry = models.DateField(auto_now=False)
    amt = models.IntegerField(default=3200)
    paymentStatus = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name_plural = "MessRegister"
        verbose_name = "MessRegister"
    

#MENU determinor classes

class FoodItems(models.Model):
    item = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.item

    class Meta:
        verbose_name_plural = "FoodItems"
        verbose_name = "FoodItem"

class Schedule(models.Model):
    day = models.DateField(auto_now=False)
    meal_type = models.CharField(max_length=10, choices=[('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Lunch')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=70.00)

    def __str__(self):
        return str(self.day)+" "+self.meal_type
    
    class Meta:
        verbose_name_plural = "Schedules"
        verbose_name = "Schedule"

class Menu(models.Model):
    scheduled_meal = models.ForeignKey(Schedule, default=None, on_delete=models.CASCADE)
    dish = models.ManyToManyField(FoodItems)

    def __str__(self):
        return str(self.scheduled_meal)

    class Meta:
        verbose_name_plural = "Menu"
        verbose_name = "Menu"


#feedback mechanism for customers 
class Feedback(models.Model):
    feedback = models.TextField(max_length=500)
    dateOfFeedback = models.DateField(auto_now_add=True)
    meal_id = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return str(self.meal_id)
