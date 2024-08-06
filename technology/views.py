from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Product_Card,Testimonial


# Create your views here.

def home(request):
    context ={'productcard': Product_Card.objects.all(),
              'testimonial': Testimonial.objects.all(),
              
         }
    
    return render(request, "home.html", context)


