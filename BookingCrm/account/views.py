from django.shortcuts import render
from django.http import HttpResponse
from .models import *;

# Create your views here.

def home(request):
    booking = Booking.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_booking = booking.count()
    
    delivered = booking.filter(status='Delivered').count()
    pending = booking.filter(status='Pending').count()
    context = {'booking': booking, 'customers': customers,
               'total_customers': total_customers, 'total_booking': total_booking,'deliverd' : delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def product(request):
    product = Drone.objects.all()
    total_droens = product.count()
    print(total_droens)
    context = {'product': product, 'total_droens': total_droens}
    return render(request,'accounts/products.html',context)


def customer(request):
    customer = Customer.objects.all()
    booking = Booking.objects.all()
    context = {'customer': customer,'booking':booking}
    return render(request, 'accounts/customers.html', context)
