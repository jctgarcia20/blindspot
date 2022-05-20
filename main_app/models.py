from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here

class Car(models.Model):
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.IntegerField()
  engine = models.CharField(max_length=50)
  mileage = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.make} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Review(models.Model):
  description = models.CharField(max_length=1500)
  rating = models.CharField(max_length=10)
  date = models.DateField(auto_now_add=True)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.make} ({self.id})'

  class Meta:
    ordering = ['-date']

  def get_absolute_url(self):
    return reverse('reviews_detail', kwargs={'review_id': self.id})

class Comment(models.Model):
  description = models.CharField(max_length=150)
  date = models.DateField(auto_now_add=True)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.make} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'comment_id': self.id})

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"