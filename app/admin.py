from django.contrib import admin

from .models import *

admin.site.register(Brand)
admin.site.register(Depot)
admin.site.register(Car)
admin.site.register(Bike)
admin.site.register(Rent)