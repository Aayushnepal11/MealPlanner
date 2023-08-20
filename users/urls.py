from . import views
from django.urls import path

app_name="users"
urlpatterns= [
    path('register/', views.RegisterView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path("home/", views.UserHomePageView.as_view(), name="home"),
    path('goals/', views.GoalPageView.as_view(),name='goals'),
    path('exercise/', views.ExercisePageView.as_view(),name='exercise'),
    path('meals/', views.MealsPageView.as_view(),name='meal'),
    path('recommendations/', views.DietRecommendationView.as_view(), name='recommendations'),
]