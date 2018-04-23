from django.contrib import admin
from .models import *
# Register your models here.


class AdminHome(admin.ModelAdmin):
    pass


admin.site.register(Jewellery, AdminHome)