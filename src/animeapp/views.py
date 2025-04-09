import requests
from django.core.paginator import Paginator
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

    paginator = Paginator(resultados, 10)  # Mostrar 10 resultados por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'animeapp/home.html', {'animes': resultados})

