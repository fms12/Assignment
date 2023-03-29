from django.contrib import admin
from .models import Customer,Location,Booking,Drone
# Register your models here.

admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(Drone)