from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Pet


class PetListView(ListView):
	model = Pet
	template_name = 'home.html'
	context_object_name = 'pets'
	ordering = ['-date_added']
	paginate_by = 5



class PetDetailView(DetailView):
	model = Pet
	template_name = 'pet_detail.html'


class PetCreateView(LoginRequiredMixin, CreateView):
	model = Pet
	template_name = 'pet_form.html'
	fields = ['name', 'description', 'birth_date']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)


class PetUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Pet
	template_name = 'pet_form.html'
	fields = ['name', 'description', 'birth_date']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		pet = self.get_object()
		if self.request.user == pet.owner:
			return True
		return False


class PetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Pet
	template_name = 'pet_confirm_delete.html'
	fields = ['name', 'description', 'birth_date']
	success_url = '/pet'


	def test_func(self):
		Pet = self.get_object()
		if self.request.user == Pet.owner:
			return True
		return False


