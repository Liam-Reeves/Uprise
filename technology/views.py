from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from .models import Product_Card,Testimonial, Carousel_Slide
from .forms import ContactForm


# Create your views here.

def home(request):
    contactform = ContactForm()
    context ={'productcard': Product_Card.objects.all(),
              'testimonial': Testimonial.objects.all(),
              'contactform': contactform,
              'home_slide': Carousel_Slide.objects.all(),
              
         }
    contactform = ContactForm()
    if request.method == 'POST':
        contactform = ContactForm(request.POST)

    if contactform.is_valid():
       name = contactform.cleaned_data['name']
       email = contactform.cleaned_data['email']
       message = contactform.cleaned_data['message']
       
       return redirect ('contact_success')
    else:
        contactform = ContactForm()
    
    return render(request, "home.html", context)

def contact_success(request):
    return render(request, "contact_success.html")

def product(request):
    context = {
        
    }
    return render(request, "products.html")



