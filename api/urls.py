from django.urls import path
from . import views

urlpatterns = [
    path('v1/users/', views.users_list),
    path('v1/users/<int:pk>/', views.user_detail),
    path('v1/pets/', views.pets_list),
    path('v1/pets/<int:pk>/', views.pet_detail),
]