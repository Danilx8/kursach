from django.shortcuts import render
from .models import *


def home(request):
    brands = Brand.objects.all().order_by("name")

    return render(request, 'home.html', {
        "title": "Домашняя страница",
        "brands": brands,
    })


def bikes(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes.html', {
        "title": "Аренда велосипеда",
        "bikes": bikes,
    })


def cars(request):
    cars = Car.objects.all()

    return render(request, 'cars.html', {
        "title": "Аренда автомобиля",
        "cars": cars
    })


def depots(request):
    depots = Depot.objects.all()

    return render(request, 'depots.html', {
        "title": "Все депо",
        "depots": depots
    })


def vehicles_by_depot(request, id):
    depot = Depot.objects.get(id=id)
    cars = Car.objects.filter(depot=depot)
    bikes = Bike.objects.filter(depot=depot)

    return render(request, 'current_depot.html', {
        "title": "Наполнение депо",
        "cars": cars,
        "bikes": bikes,
        "depot": depot,
        "count": cars.count() + bikes.count()
    })


def cars_experience(request, id):
    car = Car.objects.get(id=id)
    drives = Rent.objects.filter(car=car).count()

    return render(request, 'experience.html', {
        "title": "Количество поездок",
        "car": car,
        "count": drives
    })


def bikes_experience(request, id):
    bike = Bike.objects.get(id=id)
    drives = Rent.objects.filter(bike=bike).count()

    return render(request, 'experience.html', {
        "title": "Количество поездок",
        "bike": bike,
        "count": drives
    })
