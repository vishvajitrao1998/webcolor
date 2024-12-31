from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home_page'),
    path('rgb-to-hex', rgbtohex, name='rgbtohex'),
    path('hex-to-rgb', hextorgb, name='hextorgb'),
    path('color-palette', color_palette, name='color_palette'),
    path('color-palette/<str:name>', individual_color_palette, name='individual_category_color_palette'),
    path('color-chart', color_chart, name='color_chart'),
    path('color-chart/web-safe-color-chart', web_safe_colors, name='web_safe_colors'),
    path('contact', contact_us, name='contact_us'),
    path('about', about_us, name='about_us'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
