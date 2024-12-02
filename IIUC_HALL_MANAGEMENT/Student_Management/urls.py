from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registration/',views.Student_Registration,name='registration'),
    path('login/',views.student_login,name='login'),
    path('profile/',views.student_profile),
    
]
