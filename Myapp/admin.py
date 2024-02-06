from django.contrib import admin
from .models import User , UserProfile  # Import your models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()
    list_display =('email','username' , 'first_name' , 'last_name', 'role' , 'is_active' )
    ordering = ('date_joined' ,)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)  # Register your models here

# Register your models here.
