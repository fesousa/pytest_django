from django.shortcuts import render
from django.http import HttpResponse
from .utils.utils import calculaMediaFinal

# Create your views here.
def index(request):
    media = calculaMediaFinal(10, 8)
    return HttpResponse(media)
