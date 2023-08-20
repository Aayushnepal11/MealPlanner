from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

GENDER = [
    ("male","Male"),
    ("female","Female"),
    ("others","Others"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    gender = models.CharField(max_length=10,choices=GENDER)
    phone = models.CharField(max_length=15, null=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name_plural = "Goals"


class Exercise(models.Model):
    goal = models.ForeignKey(Goals, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    duration = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Exercise"


class Meals(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Meal"