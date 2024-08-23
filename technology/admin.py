from django.contrib import admin
from django.db import models
from .models import Product_Card, Testimonial, Carousel_Slide
# Register your models here.

admin.site.register(Product_Card)
admin.site.register(Testimonial)
admin.site.register(Carousel_Slide)
