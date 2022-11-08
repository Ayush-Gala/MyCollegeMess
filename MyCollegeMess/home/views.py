from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import students, Mess, Menu, Schedule, FoodItems, Feedback
from django.contrib import messages
from django.db import connection
# Create your views here.

#view for login
def login(request):
    return render(request, 'login.html')


#user homepage view
def homepage(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        if students.objects.filter(username=username, password=password).exists():
            student = students.objects.get(username=username)
            customer = Mess.objects.get(customer = student)
            lunchschedule = Schedule.objects.get(meal_type='Lunch', day=datetime.today().date())
            dinnerschedule = Schedule.objects.get(meal_type='Dinner', day=datetime.today().date())
            cursor = connection.cursor()
            cursor.execute("select item from home_fooditems where id in (select fooditems_id from home_menu_dish where menu_id = (select id from home_menu where scheduled_meal_id = (select id from home_schedule where meal_type='Lunch' and day='2022-11-03')));")
            lunch = cursor.fetchall()
            cursor.execute("select item from home_fooditems where id in (select fooditems_id from home_menu_dish where menu_id = (select id from home_menu where scheduled_meal_id = (select id from home_schedule where meal_type='Dinner' and day='2022-11-03')));")
            dinner = cursor.fetchall()
            cursor.close()
            return render(request, 'home.html', {'customer': customer, 'lunch': lunchschedule, 'dinner':dinnerschedule, 'lunchmenu':lunch, 'dinnermenu':dinner})

        else:
            messages.error(request, 'Please enter the correct login credentials')
            return redirect('login')


# view for signout
def signout(request):
    return redirect('login')


#view for feedback submission
def feedback(request):
    #getting fields from the customer
    current_day = datetime.today().date()
    feedback = request.POST['fdbck']
    type = request.POST['type']

    #searching for meal_id from database
    cursor = connection.cursor()
    cursor.execute("select id from home_schedule where day='{0}' and meal_type = '{1}';".format(current_day, type))
    menu_id = cursor.fetchone()
    cursor.close()
    
    #creating a schedule instance 
    instance = Schedule.objects.get(id__in=menu_id)
    #creating a feedback log
    log = Feedback(dateOfFeedback=current_day,feedback=feedback,meal_id=instance)
    log.save()
    return HttpResponse('Feedback submitted successfully. Press back button to go back to homepage!')