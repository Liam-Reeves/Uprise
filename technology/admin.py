from django.contrib import admin
from django.db import models
from .models import Product_Card, Testimonial
# Register your models here.

admin.site.register(Product_Card)
admin.site.register(Testimonial)
