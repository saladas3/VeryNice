from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.register, name="register"),
    path('Login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('Logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
