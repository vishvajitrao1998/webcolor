from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID field
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    is_active = models.BooleanField(default=True)  # New field for active status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class ColorPalette(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID field
    name = models.CharField(max_length=500)  # Name of the palette
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="palettes")
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="palettes")
    likes = models.PositiveIntegerField(default=0, verbose_name="Number of Likes")  # New field for likes
    is_active = models.BooleanField(default=True)  # New field for active status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes
    
    class Meta:
        verbose_name = "Color Palette"
        verbose_name_plural = "Color Palettes"

class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID field
    palette = models.ForeignKey(ColorPalette, on_delete=models.CASCADE, related_name="colors")
    hex_code = models.CharField(max_length=7)  # HEX format, e.g., #FFFFFF
    name = models.CharField(max_length=100, blank=True, null=True)  # Optional color name


    def __str__(self):
        return self.hex_code
    

    def hex_to_rgb(self):
        """
        Converts the HEX color code to an RGB tuple.
        """
        hex_code = self.hex_code.lstrip('#')  # Remove '#' from the start if present
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))  # Convert HEX to RGB
    

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"




