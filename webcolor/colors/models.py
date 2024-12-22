from django.db import models

# Create your models here.


# Model to store color palette details 

class ColorPaletteCategory(models.Model):

    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_url = models.SlugField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    