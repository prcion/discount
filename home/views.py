from django.shortcuts import render
from django.http import HttpResponse
from .models import Discount
def home(request):
    discount = Discount.objects.all()
    return render(request, "home/home.html", {"discount":discount,
    "title":"Discount",
    })
