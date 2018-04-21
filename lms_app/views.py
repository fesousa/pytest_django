from django.shortcuts import render
from django.http import HttpResponse
from .utils.utils import calculaMediaFinal
from .models.disciplinas import Disciplina


# Create your views here.
def index(request):
    media = calculaMediaFinal(10, 8)
    ativas = Disciplina.objects.disciplinas_ativas()
    return HttpResponse(ativas)
