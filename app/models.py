from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Vehicle(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	brand = models.ForeignKey(
		'Brand',
		models.CASCADE,
		null=True
	)
	depot = models.ForeignKey(
		'Depot',
		models.DO_NOTHING
	)
	costPerHour = models.PositiveIntegerField(
		default=0
	)
	costDaily = models.PositiveIntegerField(
		default=0
	)

	class Meta:
		abstract = True


class Bike(Vehicle):
	class Meta:
		verbose_name = 'Велосипед'
		verbose_name_plural = 'Велосипеды'


class Car(Vehicle):
	class Meta:
		verbose_name = 'Автомобиль',
		verbose_name_plural = 'Автомобили'


class Brand(models.Model):
	class ProductionType(models.TextChoices):
		BICYCLE = "Велосипед",
		CAR = "Автомобиль",
		ANY = "Любое транспортное средство"

	name = models.CharField(max_length=50)
	type = models.TextField(choices=ProductionType.choices)

	class Meta:
		verbose_name = 'Бренд',
		verbose_name_plural = 'Бренды'


class Depot(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	capacity = models.PositiveIntegerField()

	class Meta:
		verbose_name = 'Депо'
		verbose_name_plural = 'Депо'


class Rent(models.Model):
	start = models.DateTimeField(default=timezone.now)
	end = models.DateTimeField(null=True)
	Car = models.ManyToManyField(
		to=Car
	)
	Bike = models.ManyToManyField(
		to=Bike
	)
	client = models.ForeignKey(
		to=User,
		on_delete=models.DO_NOTHING
	)
	is_finished = models.BooleanField(default=False)
	final_price = models.PositiveIntegerField(default=0)

	class Meta:
		verbose_name = 'Аренда',
		verbose_name_plural = 'Аренды'