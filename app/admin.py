from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(DietCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at",]
    search_fields = ["name",]

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "image",]
    search_fields = ["title",]

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "email","phone_number", "message"]
    search_fields = ["customer_name", "email","phone_number"]