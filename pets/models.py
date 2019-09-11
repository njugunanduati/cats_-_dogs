from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Pet(models.Model):
	name = models.CharField(max_length=100)
	pet_type = models.CharField(max_length=10)
	description = models.TextField()
	birth_date = models.DateTimeField()
	date_added = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('pet-detail', kwargs={'pk':self.pk})
		