from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.register_view, name="user-register"),
]
