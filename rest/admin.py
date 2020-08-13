from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Person,Country,State,City,Town)
class RestAdmin(admin.ModelAdmin):
    pass
