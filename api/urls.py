from django.urls import path
from . import views

urlpatterns = [
	path('v1/login/', views.login),
    path('v1/user/', views.user),
    path('v1/add_pet/', views.add_pet),
    path('v1/pets/', views.pets),
    path('v1/pets/<int:pk>/', views.pet),
]