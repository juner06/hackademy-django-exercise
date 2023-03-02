from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import User



admin.site.site_header = "June Rebayla's Admin Page" 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'description']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def active(self, obj):
        return obj.is_active ==1
  
    active.boolean =True

    def has_delete_permission(self, request, obj =None):
        return True


admin.site.register(Profile, ProfileAdmin)