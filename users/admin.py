from django.contrib import admin
from .models import Profile, Goals, Exercise, Meals

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone', 'gender']
    search_fields = ['user__email', 'gender', 'phone']

@admin.register(Goals)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description']
    search_fields = ['user__username', 'title']

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['goal', 'title', 'description']
    search_fields = ['goal__username', 'title']

@admin.register(Meals)
class MealAdmin(admin.ModelAdmin):
    list_display = ['exercise', 'meal_name', 'description']
    search_fields = ['exercise__title', 'title']