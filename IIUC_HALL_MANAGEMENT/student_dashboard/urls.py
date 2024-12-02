from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('login/',views.meal_login,name='meal_login'),
    path('meal/',views.meal_management,name='meal_management'),
]