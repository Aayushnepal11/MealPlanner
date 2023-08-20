from . import views
from django.urls import *

app_name="meal_planner"
urlpatterns = [
    path("",views.HomePageView.as_view(),name="home"),
    path("contact/",views.ContactPageView.as_view(),name="contact"),
]
