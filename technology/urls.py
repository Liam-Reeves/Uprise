from  django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name="home"),
    path('', views.product, name="product"),
    path('', views.contact_success, name="contact_success"),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)