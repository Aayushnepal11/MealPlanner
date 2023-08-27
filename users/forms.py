from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER = [
    ("", "----- Select your Gender -----"),
    ("male", "Male"),
    ("female", "Female"),
    ("others", "Others"),
]

class UserRegister(UserCreationForm):
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'phone_number'}))
    gender = forms.ChoiceField(choices=GENDER)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email','phone','gender', 'password1', 'password2']


GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

FOOD_CHOICES = [
    ('vegan', 'Vegan'),
    ('vegetarian', 'Vegetarian'),
    ('non-vegetarian', 'Non-Vegetarian')
]


class HealthForm(forms.Form):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    age = forms.IntegerField(min_value=0)
    weight = forms.DecimalField(min_value=0, max_digits=5, decimal_places=2)
    height = forms.DecimalField(min_value=0, max_digits=6, decimal_places=2)
    food_category = forms.ChoiceField(choices=FOOD_CHOICES, widget=forms.RadioSelect)