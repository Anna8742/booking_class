from django.contrib import admin
from .models import Parent, Child, SwimClass, Booking

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SwimClass)
admin.site.register(Booking)
