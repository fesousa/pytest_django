from django.urls import path

from . import views

urlpatterns = [
    path('lms', views.index, name='index'),
]