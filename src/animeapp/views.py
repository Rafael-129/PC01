import requests
from django.shortcuts import render

def buscar_anime(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        url = f'https://api.jikan.moe/v4/anime?q={query}&limit=10'
        response = requests.get(url)
        if response.status_code == 200:
            resultados = response.json().get('data', [])
        else:
            print(f"Error en la API: {response.status_code}")  # Esto te ayudará a depurar si la API no responde correctamente
    return render(request, 'animeapp/home.html', {'animes': resultados})

