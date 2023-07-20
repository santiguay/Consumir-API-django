from django.shortcuts import render
import requests

# Create your views 
'''Obtain the URL of the API and return it to the template. As in a JSON (JavaScript Object Notation), we need to handle it in the template.'''
def home(request, id):
    url = f'https://rickandmortyapi.com/api/character/{id}'
    response = requests.get(url)

    if response.status_code == 200:
        personaje = response.json()  # Convertir la respuesta  a JSON 
    else:
        personaje = None

    return render(request, 'index.html', {'personaje': personaje}) 