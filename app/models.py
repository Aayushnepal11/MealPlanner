from django.db import models

# Create your models here.
class DietCategory(models.Model):
    name = models.CharField(max_length=155)
    created_at = models.DateField(auto_now=True, editable=False) 
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "Diet Category"

    def __str__(self):
        return self.name
    
class FoodCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="services", blank=True)

    class Meta:
        verbose_name_plural = "Food Category"

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    message = models.TextField()
