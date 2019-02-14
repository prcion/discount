from django.contrib import admin
from .models import Discount

@admin.register(Discount)

class AdminCreate(admin.ModelAdmin):
    lista_display = ["id"]
