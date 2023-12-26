from django.contrib import admin
from .models import Capsule, picked_capsule

class CapsuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'content', 'picture', 'destination', 'write_date', 'open_date') 

admin.site.register(Capsule, CapsuleAdmin)
admin.site.register(picked_capsule)