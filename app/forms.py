from django import forms
from .models import Feedback

class UserForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'