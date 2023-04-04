from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PropertyListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    built_up_area_in_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    is_for_sale = models.BooleanField(default=True)
    is_for_rent = models.BooleanField(default=False)
    list_date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_main = models.ImageField(upload_to='photos')
    photo_1 = models.ImageField(upload_to='photos', blank=True)
    photo_2 = models.ImageField(upload_to='photos', blank=True)
    photo_3 = models.ImageField(upload_to='photos', blank=True)
    photo_4 = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return self.title

class PropertyInquiry(models.Model):
    listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inquiry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.listing.title} by {self.user.username}"

# class Inquiry(models.Model):
#     listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     message = models.TextField(blank=True)
#     inquiry_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Inquiry for {self.listing} by {self.user.username}'