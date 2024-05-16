from django.contrib import admin

from .models import Booking, Guest, Hotel, Room

admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
