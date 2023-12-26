from django.contrib import admin
from .models import Capsule

class CapsuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'content', 'picture', 'destination', 'write_date', 'open_date') 

admin.site.register(Capsule, CapsuleAdmin)
