from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'/home/pedro_cardoso/alura-space/templates/galeria/index.html')

def imagem(request):
    return render(request, '/home/pedro_cardoso/alura-space/templates/galeria/imagem.html')