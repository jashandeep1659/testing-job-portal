from django.contrib import admin

# Register your models here.
from .models import *
class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)

admin.site.register(User,UserAdmin)


