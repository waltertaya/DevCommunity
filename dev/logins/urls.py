from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('login/', views.login, name='login-page'),
]
