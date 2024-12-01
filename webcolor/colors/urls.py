from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
