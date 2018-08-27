from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo,Aadhar, Vehicle
# Register your models here.

admin.site.register(Todo)
admin.site.register(Aadhar)
admin.site.register(Vehicle)