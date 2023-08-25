from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegister, HealthForm
from django.views.generic import FormView, View, TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from  django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from . import csv_file_reader
import random

class RegisterView(FormView):
    form_class = UserRegister
    template_name = "registration/register.html"


    def form_valid(self, form):
        user = form.save(self.request.POST)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        user.profile.gender=form.cleaned_data['gender']
        user.profile.phone=form.cleaned_data['phone']
        user.profile.save()
        current_site = get_current_site(self.request)
        subject = "Activate Your Account"
        message = render_to_string(
            'auth/activation_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            },
        )
        user.email_user(subject, message)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('meal_planner:home')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.profile.email_confirmed = True
            user.is_active = True
            user.save()
            return render(request, 'auth/account_activated.html')
        else:
            return render(request, 'auth/activation_invalid.html')


class LogoutView(LogoutView):
    template_name = "registration/logged_out.html"
    
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return render(self.request, self.template_name)

class LoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        return reverse("users:home")

class UserHomePageView(FormView):
    template_name = "login_auth/user_index.html"
    form_class = HealthForm

    def form_valid(self, form):
        user_inputs = {
            'gender': form.cleaned_data['gender'],
            'age': form.cleaned_data['age'],
            'weight': form.cleaned_data['weight'],
            'height ': form.cleaned_data['height'],
            'generic_disease': form.cleaned_data['generic_disease'],
            'food_category': form.cleaned_data['food_category'],
        }
        meals = csv_file_reader.load_csv_data('users\meal.csv')
        suggested_meals = [meal for meal in meals if meal['Type'].lower() == user_inputs['food_category']]
        return HttpResponse(suggested_meals)

        if suggested_meals:
            random.shuffle(suggested_meals)
            meals_count = len(suggested_meals)
            breakfast_meal = suggested_meals[random.randint(0, meals_count - 1)]
            lunch_meal = suggested_meals[random.randint(0, meals_count - 1)]
            dinner_meal = suggested_meals[random.randint(0, meals_count - 2)]

            workout_suggestions = csv_file_reader.get_workout_suggestions(user_inputs)
        
            self.request.session['recommendations'] = {
                'breakfast_meal': breakfast_meal,
                'lunch_meal': lunch_meal,
                'dinner_meal': dinner_meal,
                'workout_suggestions': workout_suggestions,
            }

        return redirect("users:recommendations")
    
    
      
      
class DietRecommendationView(TemplateView):
    template_name="login_auth/recommendation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recommendations = self.request.session.get('recommendations', {})
        context.update(recommendations)
        return context




