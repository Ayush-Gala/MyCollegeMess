from django.contrib import admin
from home.models import students, Mess, FoodItems, Schedule, Menu, Feedback

# Register your models here.
admin.site.register(students)
admin.site.register(Mess)
admin.site.register(FoodItems)
admin.site.register(Schedule)
admin.site.register(Menu)
admin.site.register(Feedback)