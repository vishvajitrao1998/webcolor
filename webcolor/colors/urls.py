from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home_page'),
    path('rgb-to-hex', rgbtohex, name='rgbtohex'),
    path('hex-to-rgb', hextorgb, name='hextorgb'),
    path('color-palettes', color_palettes, name='color_palettes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
