from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),
    path(
        'home/',
        views.home,
        name='home'
    ),
    path(
        'bikes/',  # урл для posts
        views.bikes,   # вызываем класс представления как вью
        name='bikes'
    ),
    path(
        'cars/',  # урл для posts
        views.cars,   # вызываем класс представления как вью
        name='cars'
    ),
    path(
        'depots/',
        views.depots,
        name='depots'
    ),
    path(
        'depots/<int:id>',  # урл для posts
        views.vehicles_by_depot, # вызываем класс представления как вью
        name='vehicles in depot'
    ),
    path(
        'depots/cars/<int:id>',
        views.cars_experience,
        name='cars experience'
    ),
    path(
        'depots/bikes/<int:id>',
        views.bikes_experience,
        name='bikes experience'
    )
]