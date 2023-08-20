from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import *
from .forms import UserForm
from django.contrib import messages
# Create your views here.
class HomePageView(ListView):
    model = FoodCategory
    template_name = "meal_planner/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = self.model.objects.all() 
        return context

class ContactPageView(View):
    template_name = "meal_planner/contact.html"
    initial = {"key": "value"}
    model = Feedback
    form_class = UserForm
    success_url = "/contact"

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Uploaded Successfully")
            return redirect("meal_planner:contact")
        return render(request, self.template_name, {"form": form})
