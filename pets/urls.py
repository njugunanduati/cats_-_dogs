from django.urls import path
from .views import PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView


urlpatterns = [
	path('', PetListView.as_view(), name='pets-home'),
	path('<int:pk>', PetDetailView.as_view(), name='pet-detail'),
	path('new', PetCreateView.as_view(), name='pet-create'),
	path('pet/<int:pk>/update/', PetUpdateView.as_view(), name='pet-update'),
	path('pet/<int:pk>/delete/', PetDeleteView.as_view(), name='pet-delete'),
]
