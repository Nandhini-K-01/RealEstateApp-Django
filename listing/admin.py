from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.PropertyListing),
admin.site.register(models.PropertyInquiry),