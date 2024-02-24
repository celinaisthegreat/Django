from django.shortcuts import render
from .models import Food

# Create your views here.
def index(request):
    food_details = Food.objects.all()
    data = {
        "food_details" : food_details
    }
    return render(request, "index.html", data)