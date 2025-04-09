import requests
from django.shortcuts import render

# Create your views here.
def buscar_anime(request):
    query =request.Get.get('q')
    resulador = []
    if query:
         url = f'https://api.jikan.moe/v4/anime?q={query}&limit=10'
         response = request.get(url)
         
         if response.status_code == 200:
              resultados = response.json().get('data', [])
    return render(request, "animeap/home.html", {'anmesapp': resultados})
