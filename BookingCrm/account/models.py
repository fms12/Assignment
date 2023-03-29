from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.address_line_1}"


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # profile_pic = models.ImageField(
    #     default='profile.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # it gives how the actually file look like
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)


class Drone(models.Model):
    drone_id = models.CharField(max_length=20, unique=True)
    name_drone = models.CharField(max_length=200)
    price_drone = models.FloatField(null=True)
    battery_percentage = models.IntegerField()
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(max_length=200, null=True)
    # location = models.ForeignKey(Location, max_length=200)
    # tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name_drone



# one to many realtionship
class Booking(models.Model):
    BOOKING_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('D', 'Delivered')
    )
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=BOOKING_STATUS_CHOICES, default='')

    def __str__(self):
        return f"{self.customer}, {self.drone}, {self.status}"
