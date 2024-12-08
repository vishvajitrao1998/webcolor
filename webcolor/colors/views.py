from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def rgbtohex(request):
    return render(request, 'rgb-to-hex.html')


def hextorgb(request):
    return render(request, 'hex-to-rgb.html')


def color_palettes(request):
    return render(request, 'color-palettes.html')
